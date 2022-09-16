# Generated by Django 3.2.14 on 2022-09-15 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_remove_job_skillset_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skillset_required',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.skill'),
            preserve_default=False,
        ),
    ]