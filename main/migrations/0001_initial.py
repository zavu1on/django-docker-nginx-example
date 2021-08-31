# Generated by Django 3.2.6 on 2021-08-28 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_checked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 8, 28, 22, 21, 8, 145111))),
            ],
        ),
    ]
