from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала", default="09:00")
    end_time = models.TimeField(verbose_name="Время окончания", default="12:00")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=100, verbose_name="Локация", default="Не указан")
    address = models.CharField(max_length=200, verbose_name="Адрес", default="Не указан")
    location_details = models.CharField(max_length=100, verbose_name="Уточнение локации", default="Не указано")  # Новое поле
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"