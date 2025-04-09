# Generated by Django 5.1.6 on 2025-04-09 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_image_event_additional_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название активности')),
                ('start_time', models.TimeField(verbose_name='Время начала')),
                ('end_time', models.TimeField(verbose_name='Время окончания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('location', models.CharField(default='Не указан', max_length=100, verbose_name='Локация')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='events.event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Активность мероприятия',
                'verbose_name_plural': 'Активности мероприятия',
            },
        ),
    ]
