# Generated by Django 3.2.5 on 2021-09-08 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0011_alter_thoughtsbyuser_posted_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thoughtsbyuser',
            name='posted_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 16, 41, 36, 794598)),
        ),
    ]
