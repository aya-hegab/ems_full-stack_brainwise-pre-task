from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    num_departments = serializers.SerializerMethodField()
    num_employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'num_departments', 'num_employees']
        
    def get_num_departments(self, obj):
        return obj.num_departments

    def get_num_employees(self, obj):
        return obj.num_employees