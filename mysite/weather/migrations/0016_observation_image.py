# Generated by Django 2.2.4 on 2019-09-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0015_auto_20190805_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
