# Generated by Django 5.0.4 on 2024-04-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_staff_remove_booking_guest_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.AddField(
            model_name='booking',
            name='are_you_aware_of_what_you_need_to_do_to_achieve_these_goals',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='do_you_feel_you_have_achieved_the_goals_you_set_last_year',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='explain_how_you_have_or_why_you_have_managed_to_achieve_these_goals',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='how_do_you_feel_about_your_job_and_the_company',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='is_there_any_equipment_or_training_to_help_you_in_your_role',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='what_are_your_achievable_goals_for_the_next_12_months',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='what_would_you_change_if_you_could',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='which_parts_of_your_job_are_doing_well_and_where_do_you_think_you_could_improve',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='how_well_they_think_they_are_doing_on_the_job',
            field=models.TextField(default=''),
        ),
    ]