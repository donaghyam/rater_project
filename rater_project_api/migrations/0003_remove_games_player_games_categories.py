# Generated by Django 4.0.4 on 2022-05-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater_project_api', '0002_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='player',
        ),
        migrations.AddField(
            model_name='games',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='rater_project_api.categories'),
        ),
    ]
