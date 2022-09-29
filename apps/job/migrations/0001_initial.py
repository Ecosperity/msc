# Generated by Django 3.2.14 on 2022-09-29 09:26

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('job_title', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('job_description', tinymce.models.HTMLField()),
                ('experience', models.CharField(max_length=50)),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('no_of_openings', models.PositiveSmallIntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('functional_area', models.CharField(max_length=100)),
                ('employement_type', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Freelancing', 'Freelancing'), ('Contract', 'Contract')], default='Full time', max_length=50)),
                ('country', models.CharField(choices=[('India', 'India'), ('Italy', 'Italy'), ('Switzerland', 'Switzerland'), ('USA', 'USA')], max_length=50)),
                ('place', models.CharField(blank=True, max_length=50)),
                ('visit_count', models.PositiveIntegerField(default=0)),
                ('job_applied_count', models.PositiveIntegerField(default=0)),
                ('publish', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Job Post',
                'verbose_name_plural': 'Job Posts',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_applied', models.BooleanField(default=False)),
                ('notice_period', models.CharField(max_length=20)),
                ('linkedin_link', models.URLField(max_length=100)),
                ('qualitative_skills', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/%Y/%m/%d/')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('job', models.ManyToManyField(to='job.Job')),
            ],
        ),
    ]
