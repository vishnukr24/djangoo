# Generated by Django 5.0.3 on 2024-08-07 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
    ]