from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from . import models as payment_models
from . import forms as payment_forms
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin
from .models import Payment, Invoice
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from .forms import PaymentForm


# test function
def user_belongs_to_staff_group(user):
    if user in Group.objects.get(name='Staff').user_set.all():
        return True
    else:
        return False


# secured
class PaymentList(UserPassesTestMixin, ListView):
    model = Payment

    ordering = ['-Payment.invoice.pk']
    template_name = 'payment_list.html'

    def test_func(self):
        if self.request.user in Group.objects.get(name='Patient').user_set.all():
            return True
        else:
            return False

    def get_queryset(self):
        return Payment.objects.filter(invoice__patient__pk=self.request.user.pk).all()


# secured
class MakePayment(UserPassesTestMixin, DetailView):
    model = Invoice
    template_name = 'make_payment.html'

    def test_func(self):
        if self.request.user in Group.objects.get(name='Patient').user_set.all():
            return True
        else:
            return False


# secured
class InvoiceListAll(UserPassesTestMixin, ListView):

    def test_func(self):
        if self.request.user in Group.objects.get(name='CEO').user_set.all() or self.request.user in Group.objects.get(
                name='Staff').user_set.all():
            return True
        else:
            return False

    model = Invoice
    ordering = ['date_billed']
    template_name = 'invoice_list_all.html'


class InvoiceListUser(UserPassesTestMixin, ListView):

    def test_func(self):
        if self.request.user in Group.objects.get(name='Patient').user_set.all():
            return True
        else:
            return False

    model = Invoice
    ordering = ['date_billed']
    template_name = 'invoice_list_user.html'


# secured
@login_required()
@user_passes_test(user_belongs_to_staff_group)
def MakeCashPayment(request, ):
    if request.method == 'POST':
        form = payment_forms.PaymentForm(request.POST)
        if form.is_valid():
            try:
                form = form.clean()
                # updating invoice information
                updated_invoice = payment_models.Invoice.objects.get(pk=form.get('invoice_number'))

                prev_amount_owed = updated_invoice.amount_owed

                new_amount_owed = prev_amount_owed - form.get('payment_amount')

                if new_amount_owed < 0 or new_amount_owed >= prev_amount_owed:

                    messages.add_message(request, messages.WARNING,
                                         'Amount can not be negative, greater than or the same as the previous amount owed.')

                    return redirect('cash-payment')
                else:

                    updated_invoice.amount_owed = new_amount_owed

                    # creating new cash payment
                    Payment(invoice=updated_invoice, payment_amount=form.get('payment_amount'),).save()
                    updated_invoice.save()
                    messages.add_message(request, messages.SUCCESS, 'Payment Successful. Amount Owed Updated.')
            except:

                messages.add_message(request, messages.WARNING, 'Something Went Wrong. Try Again')

            return redirect('invoice-list-all')
    else:
        form = payment_forms.PaymentForm()

    context = {'form': form}
    return render(request, 'cash_payment.html', context=context)





## Unsuccessful attempt to turn cash payments into a Class Based View
# class MakeCashPayment(UserPassesTestMixin, CreateView):
#     model = Payment
#     template_name = 'cash_payment.html'
#     success_message = "Payment was created successfully"
#     # form_class = PaymentForm
#     fields = [
#         'invoice',
#         'payment_amount'
#     ]
#
#     def post(self, request, *args, **kwargs):
#         try:
#             form = PaymentForm(request.POST)
#             if form.is_valid():
#                 new_invoice = Invoice.objects.get(invoice=form.invoice_number)
#                 original_amount_owed = new_invoice.amount_owed
#                 if original_amount_owed >= form.payment_amount:
#                     new_invoice.amount_owed = original_amount_owed - form.payment_amount
#                     new_invoice.save()
#                     Payment(payment_amount=form.payment_amount, invoice=new_invoice)
#
#         except:
#             messages.add_message(request, level=messages.WARNING, message='Something went wrong. Please Try Again.')
#             return reverse_lazy('cash-payment-staff')
#
#         return reverse_lazy('portal')
#
#     # def post(self, request, *args, **kwargs):
#     #     form = BookCreateForm(request.POST)
#     #     if form.is_valid():
#     #         book = form.save()
#     #         book.save()
#     #         return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
#     #     return render(request, 'books/book-create.html', {'form': form})
#
#     def test_func(self):
#         return user_belongs_to_staff_group(self.request.user)


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'view_invoice.html'
    extra_context = {}



