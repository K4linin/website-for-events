# Generated by Django 5.1.6 on 2025-04-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_organizers'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, help_text='Оставьте пустым, если мероприятие длится один день', null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название партнера'),
        ),
    ]
