from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as payment_views

from . import views

urlpatterns = [

    path('view_invoice/<int:pk>/', payment_views.InvoiceDetailView.as_view(), name='invoice-detail-view'),
    path('make_payment/<int:pk>/', payment_views.MakePayment.as_view(), name='make-payment'),
    path('invoice_list_user/', payment_views.InvoiceListUser.as_view(), name='invoice-list-user'),
    path('invoice_list_all/', payment_views.InvoiceListAll.as_view(), name='invoice-list-all'),
    path('payment_list/', payment_views.PaymentList.as_view(), name='payment-list'),
    path('cash_payment/', payment_views.MakeCashPayment, name='cash-payment-staff')

    # path('pay/', payment_views.LogoutView.as_view(template_name='accounts/logout.html'), name='pay-invoice'),

]
