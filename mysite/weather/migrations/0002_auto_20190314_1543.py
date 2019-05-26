# Generated by Django 2.1.7 on 2019-03-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='aloft_wind_direction',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='aloft_wind_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='cloud_coverage',
            field=models.CharField(choices=[('Full coverage', 'Full coverage, little or no sky'), ('Heavy coverage', 'Heavy coverage, small patches of sky'), ('Medium coverage', 'Medium coverage, about half clouds and half sky'), ('Light coverage', 'Light coverage, very few clouds'), ('None', 'No clouds')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='cloud_observation',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='perceived_outdoor_humidity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='perceived_outdoor_temperature',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='surface_wind_direction',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='surface_wind_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]