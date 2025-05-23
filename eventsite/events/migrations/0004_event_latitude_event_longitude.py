# Generated by Django 5.1.6 on 2025-04-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventactivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]
