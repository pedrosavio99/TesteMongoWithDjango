# Generated by Django 4.0.5 on 2023-09-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_todo_comentariofinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='pausado',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
