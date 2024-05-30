from django.db import models
from company.models import Company

class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    @property
    def num_employees(self):
        return self.employees.count()

    def __str__(self):
        return self.name
