# Generated by Django 3.2.9 on 2022-11-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]