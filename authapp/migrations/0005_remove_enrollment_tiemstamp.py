# Generated by Django 5.0 on 2024-01-29 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_enrollment_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='tiemstamp',
        ),
    ]
