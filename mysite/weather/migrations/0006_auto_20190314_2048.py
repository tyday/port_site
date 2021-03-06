# Generated by Django 2.1.7 on 2019-03-15 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_auto_20190314_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud_coverage_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloud_coverage_short', models.CharField(max_length=255)),
                ('cloud_coverage_long', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='observation',
            name='cloud_coverage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.Cloud_coverage_choices'),
        ),
    ]
