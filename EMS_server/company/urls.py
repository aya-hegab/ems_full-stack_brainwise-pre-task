from django.urls import path
from .views import *

urlpatterns = [
        path('companies/', list_companies, name='list_companies'),
        path('companies/add/', add_company, name='add_company'),
        path('companies/update/<int:pk>/', update_company, name='update_company'),
        path('companies/delete/<int:pk>/', delete_company, name='delete_company'),
]