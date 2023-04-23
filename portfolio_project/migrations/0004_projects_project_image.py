# Generated by Django 3.2.17 on 2023-04-08 17:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_project', '0003_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
