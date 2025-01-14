# Generated by Django 5.0.3 on 2024-08-06 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doc_image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.doctor')),
            ],
        ),
    ]
