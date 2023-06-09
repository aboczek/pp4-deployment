# Generated by Django 3.2.17 on 2023-04-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_project', '0002_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('project_link', models.URLField(max_length=250)),
                ('project_description', models.TextField()),
            ],
        ),
    ]
