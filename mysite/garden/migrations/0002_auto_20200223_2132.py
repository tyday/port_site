# Generated by Django 2.2.9 on 2020-02-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorreading',
            name='timestamp',
            field=models.BigIntegerField(unique=True),
        ),
    ]