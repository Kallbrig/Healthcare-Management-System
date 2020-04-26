from django.contrib import admin
from .models import Invoice, Payment
# Register your models here.

admin.site.register(Invoice)
admin.site.register(Payment)
