# Generated by Django 2.1.3 on 2019-01-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_project_githublink'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
