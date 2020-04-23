from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as payment_views

from . import views

urlpatterns = [

    path('view_invoice/<int:pk>/', payment_views.InvoiceDetailView.as_view(), name='invoice-detail-view'),
    path('view_payment/<int:pk>/', payment_views.PaymentDetailView.as_view(), name='payment-detail-view'),
    path('invoice_list/', payment_views.InvoiceList.as_view(), name='invoice-list'),
    path('payment_list/', payment_views.PaymentList.as_view(), name='payment-list'),

    # path('pay/', payment_views.LogoutView.as_view(template_name='accounts/logout.html'), name='pay-invoice'),

]
