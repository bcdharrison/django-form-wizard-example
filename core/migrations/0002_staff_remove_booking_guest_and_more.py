# Generated by Django 5.0.4 on 2024-04-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest',
        ),
        migrations.AddField(
            model_name='booking',
            name='how_well_they_think_they_are_doing_on_the_job',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]