from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as payment_views

from . import views

urlpatterns = [
    path('view_invoice/', payment_views(template_name='invoice.html'), name='invoice-detail-view'),
    # path('view_invoice_list/', payment_views.register, name='invoice-list'),
    # path('pay/', payment_views.LogoutView.as_view(template_name='accounts/logout.html'), name='pay-invoice'),
    #

]
