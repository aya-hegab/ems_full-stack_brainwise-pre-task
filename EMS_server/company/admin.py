from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_departments', 'num_employees')

admin.site.register(Company, CompanyAdmin)
