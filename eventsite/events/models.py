from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала", default="09:00")
    end_time = models.TimeField(verbose_name="Время окончания", default="12:00")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=100, verbose_name="Локация", default="Не указан")
    address = models.CharField(max_length=200, verbose_name="Адрес", default="Не указан")
    location_details = models.CharField(max_length=100, verbose_name="Уточнение локации", default="Не указано")
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название партнера")
    logo = models.ImageField(upload_to='partners/', verbose_name="Логотип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название видео")
    video_file = models.FileField(upload_to='videos/', verbose_name="Видео файл")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    publication_date = models.DateField(verbose_name="Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"