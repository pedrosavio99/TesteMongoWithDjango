# Generated by Django 4.0.5 on 2023-07-31 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=4, unique=True)),
                ('senha', models.CharField(max_length=4)),
            ],
        ),
    ]
