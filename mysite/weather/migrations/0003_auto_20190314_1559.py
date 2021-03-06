# Generated by Django 2.1.7 on 2019-03-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20190314_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='observed_outdoor_humidity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='observed_outdoor_temperature',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='observation',
            name='observed_pressure_millibars',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
