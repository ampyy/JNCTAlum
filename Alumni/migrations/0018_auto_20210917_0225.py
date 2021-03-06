# Generated by Django 3.2.5 on 2021-09-16 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0017_alter_thoughtsbyuser_posted_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=500)),
                ('posted_time', models.DateTimeField(default=datetime.datetime(2021, 9, 17, 2, 25, 11, 945428))),
            ],
        ),
        migrations.AlterField(
            model_name='thoughtsbyuser',
            name='posted_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 2, 25, 11, 938441)),
        ),
    ]
