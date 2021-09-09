# Generated by Django 3.2.5 on 2021-09-07 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0006_auto_20210729_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThoughtsByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('thought', models.CharField(max_length=500)),
                ('posted_time', models.DateTimeField(default=datetime.datetime(2021, 9, 7, 14, 20, 30, 442435))),
            ],
        ),
    ]
