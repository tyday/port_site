# Generated by Django 2.1.7 on 2019-03-15 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0012_auto_20190314_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='phenomena_observation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.Phenomena_choice'),
        ),
    ]