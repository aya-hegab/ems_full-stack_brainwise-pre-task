from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'hired_on', 'days_employed')

admin.site.register(Employee, EmployeeAdmin)
