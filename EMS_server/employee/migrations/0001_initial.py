# Generated by Django 5.0.6 on 2024-05-29 02:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Application Received', 'Application Received'), ('Interview Scheduled', 'Interview Scheduled'), ('Hired', 'Hired'), ('Not Accepted', 'Not Accepted')], default='Application Received', max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=255)),
                ('hired_on', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='department.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
