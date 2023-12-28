# Generated by Django 5.0 on 2023-12-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_remove_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='hero',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
