# Generated by Django 5.1.6 on 2025-04-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_address_event_end_time_event_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_details',
            field=models.CharField(default='Не указано', max_length=100, verbose_name='Уточнение локации'),
        ),
    ]
