# Generated by Django 2.0.2 on 2018-03-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='email address'),
        ),
    ]
