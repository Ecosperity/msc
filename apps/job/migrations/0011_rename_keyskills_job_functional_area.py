# Generated by Django 3.2.14 on 2022-09-14 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20220914_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='Keyskills',
            new_name='functional_area',
        ),
    ]