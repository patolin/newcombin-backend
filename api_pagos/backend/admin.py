from django.contrib import admin

# Register your models here.
from backend.models import Payables, Transaction

admin.site.register(Payables)
admin.site.register(Transaction)