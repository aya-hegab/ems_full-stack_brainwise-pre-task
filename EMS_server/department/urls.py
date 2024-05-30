from django.urls import path
from .views import *

urlpatterns = [
        path('departments/', list_departments, name='list_departments'),
        path('departments/add/', add_department, name='add_department'),
        path('departments/update/<int:pk>/', update_department, name='update_department'),
        path('departments/delete/<int:pk>/', delete_department, name='delete_department'),
]