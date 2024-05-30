from rest_framework import serializers
from .models import Employee
from user_account.serializer import UserSerializer
from user_account.models import User
from company.models import Company
from department.models import Department
import re
from rest_framework.authtoken.models import Token



class EmployeeSerializer(serializers.ModelSerializer):
    days_employed = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'company', 'department', 'name', 'status', 'hired_on', 'days_employed','user','mobile_number','designation']
    
    def get_days_employed(self, obj):
        return obj.days_employed

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    mobile_number = serializers.CharField(write_only=True, required=True)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    # department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.none())
    designation = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=Employee.STATUS_CHOICES, default='Application Received')
    name = serializers.CharField(max_length=255, required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='employee')


    class Meta:
        model = Employee
        fields = ['role','name','email', 'password', 'password2', 'mobile_number', 'company', 'department', 'designation', 'status']

    def __init__(self, *args, **kwargs):
        super(EmployeeRegisterSerializer, self).__init__(*args, **kwargs)
        if 'company' in self.initial_data:
            company_id = self.initial_data['company']
            self.fields['department'].queryset = Department.objects.filter(company_id=company_id)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if not re.match(r'^\+201[0125]\d{8}$', attrs['mobile_number']):
            raise serializers.ValidationError("Mobile number must start with +2010, +2011, +2012, or +2015 and be exactly 13 digits long.")
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})

        return attrs

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        mobile_number = validated_data.pop('mobile_number')
        company = validated_data.pop('company')
        department = validated_data.pop('department')
        designation = validated_data.pop('designation')
        status = validated_data.pop('status')
        name = validated_data.pop('name')
        role = validated_data.pop('role')

        user = User(email=email)
        user.set_password(password)
        user = User(email=email, role=role)
        user.save()

        employee = Employee(
            user=user,
            mobile_number=mobile_number,
            company=company,
            department=department,
            designation=designation,
            status=status,
            name=name,
        )
        employee.save()

        return employee
    

