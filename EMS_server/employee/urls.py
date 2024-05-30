from django.urls import path
from .views import *

urlpatterns = [
        path('register/', employee_register, name='employee-register'),
        path('login/', custom_auth_token, name='login'),
        path('logout/', logout_view, name='logout'),
        path('employee-details/', user_employee_details, name='user_employee_details'),
]
