# Generated by Django 5.0 on 2024-01-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_attendance_enrollment_timestamp_trainer_timestamp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='TraineedBy',
            new_name='TrainedBy',
        ),
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(default='your_default_value_here', max_length=15),
        ),
    ]