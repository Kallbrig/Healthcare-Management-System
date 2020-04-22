from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Payment, Invoice


class PaymentList(ListView):
    model = Payment
    paginate_by = 15
    ordering = ['payment_amount']
    template_name = 'payment_list.html'


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'view_payment.html'


class InvoiceList(ListView):
    model = Invoice
    paginate_by = 15
    ordering = ['date_billed']
    template_name = 'invoice_list.html'


class InvoiceDetailView(DetailView):
    model = Payment
    template_name = 'view_invoice.html'


def makePayment():
    print('hello')
