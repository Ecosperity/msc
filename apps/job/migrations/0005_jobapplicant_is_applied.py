# Generated by Django 3.2.14 on 2022-09-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_is_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='is_applied',
            field=models.BooleanField(default=False),
        ),
    ]
