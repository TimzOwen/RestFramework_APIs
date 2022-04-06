from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','age','address','phone_number']

# Register your models here.
admin.site.register(Customer, CustomerAdmin)