# Generated by Django 5.1.6 on 2025-04-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_location_details_event_goals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.TextField(blank=True, help_text='Укажите организаторов через запятую, например: МИРЭА, МГУ', verbose_name='Организаторы'),
        ),
    ]
