from django.db import models
from datetime import date
from company.models import Company
from department.models import Department
from user_account.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.utils import timezone


class Employee(models.Model):
    STATUS_CHOICES = [
        ('Application Received', 'Application Received'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Hired', 'Hired'),
        ('Not Accepted', 'Not Accepted')
    ]
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Application Received')
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    mobile_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            today = date.today()
            return (today - self.hired_on).days
        return 0
    
    @property
    def email(self):
        return self.user.email
    
    def __str__(self):
        return self.email
    

    def clean(self): #works for the admin dashboard only
        if self.department.company != self.company:
            raise ValidationError('Department does not belong to the selected company.')
        
    


@receiver(pre_save, sender=Employee)
def update_hired_on_on_status_change(sender, instance, **kwargs):
    if instance.status == 'Hired':
        instance.hired_on = timezone.now().date()
    else:
        instance.hired_on = None



