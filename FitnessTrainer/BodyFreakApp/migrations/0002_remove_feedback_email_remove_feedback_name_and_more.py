# Generated by Django 5.0 on 2024-05-14 21:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BodyFreakApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]