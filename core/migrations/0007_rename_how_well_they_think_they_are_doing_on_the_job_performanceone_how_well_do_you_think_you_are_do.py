# Generated by Django 5.0.4 on 2024-04-29 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_performancetwo_attitude_and_effort_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performanceone',
            old_name='how_well_they_think_they_are_doing_on_the_job',
            new_name='how_well_do_you_think_you_are_doing_on_the_job',
        ),
    ]
