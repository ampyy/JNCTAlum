# Generated by Django 3.2.5 on 2021-07-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0004_verification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verification',
            name='verified',
        ),
        migrations.AddField(
            model_name='userinfobasic',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
