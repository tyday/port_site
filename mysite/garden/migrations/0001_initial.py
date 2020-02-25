# Generated by Django 2.2.9 on 2020-02-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp1', models.FloatField()),
                ('temp2', models.FloatField()),
                ('rh1', models.FloatField()),
                ('rh2', models.FloatField()),
                ('light', models.IntegerField()),
                ('timestamp', models.BigIntegerField()),
            ],
        ),
    ]