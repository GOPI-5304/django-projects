# Generated by Django 5.0 on 2023-12-12 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
    ]
