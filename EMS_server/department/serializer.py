from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ['id', 'company', 'name', 'num_employees']
    def get_num_employees(self, obj):
        return obj.num_employees
