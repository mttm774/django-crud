from django.contrib import admin
from .models import vehicle
# Register your models here.

@admin.register(vehicle)
class VehiculosAdmin(admin.ModelAdmin):
    list_display = ['id', 'placa', 'modelo','marca']