from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'num_employees')

admin.site.register(Department, DepartmentAdmin)


