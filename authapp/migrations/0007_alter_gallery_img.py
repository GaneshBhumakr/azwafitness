# Generated by Django 5.0 on 2024-01-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_gallery_remove_trainer_tiemstamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]