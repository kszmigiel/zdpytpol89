# Generated by Django 5.1.6 on 2025-03-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_image_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
