# Generated by Django 2.1.3 on 2019-01-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_project_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githublink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
