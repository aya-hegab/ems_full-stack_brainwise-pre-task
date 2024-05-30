from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    @property
    def num_departments(self):
        return self.departments.count()

    @property
    def num_employees(self):
        return self.employees.count()

    def __str__(self):
        return self.name

