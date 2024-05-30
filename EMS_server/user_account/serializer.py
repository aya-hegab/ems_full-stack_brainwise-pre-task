from rest_framework import serializers
from .models import User
from employee.models import Employee
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'is_staff']
