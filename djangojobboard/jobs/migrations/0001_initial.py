# Generated by Django 3.2.9 on 2022-11-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('remote', models.BooleanField(default=False)),
                ('salary', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
