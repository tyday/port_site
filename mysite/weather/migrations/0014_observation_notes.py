# Generated by Django 2.1.7 on 2019-03-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0013_observation_phenomena_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
