from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from . import models as payment_models
from . import forms as payment_forms
from django.contrib import messages

from .models import Payment, Invoice


class PaymentList(ListView):
    model = Payment
    paginate_by = 15
    ordering = ['payment_amount']
    template_name = 'payment_list.html'


class MakePayment(DetailView):
    model = Invoice
    template_name = 'make_payment.html'


class InvoiceList(ListView):
    model = Invoice
    paginate_by = 15
    ordering = ['date_billed']
    template_name = 'invoice_list.html'


def makeCashPayment(request, ):
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
                    updated_invoice.save()
                    # creating new cash payment
                    Payment(invoice=updated_invoice, payment_amount=form.get('payment_amount'),
                            payment_method='Cash').save()

            except:

                messages.add_message(request, messages.WARNING, 'Something Went Wrong. Try Again')

            return redirect('invoice-list')
    else:
        form = payment_forms.PaymentForm()

    context = {'form': form}
    return render(request, 'cash_payment.html', context=context)
