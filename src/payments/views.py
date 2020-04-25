
from django.views.generic import ListView, DetailView

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


# class InvoiceDetailView(DetailView):
#     model = Invoice
#     template_name = 'view_invoice.html'





