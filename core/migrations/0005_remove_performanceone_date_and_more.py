# Generated by Django 5.0.4 on 2024-04-24 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_performancetwo_rename_booking_performanceone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performanceone',
            name='date',
        ),
        migrations.RemoveField(
            model_name='performanceone',
            name='number_of_nights',
        ),
        migrations.RemoveField(
            model_name='performanceone',
            name='room_type',
        ),
    ]
