# Generated by Django 2.0.2 on 2018-04-17 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me_api', '0002_auto_20180407_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='name',
        ),
    ]
