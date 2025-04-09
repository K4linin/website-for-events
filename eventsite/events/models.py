from django.db import models
from django.utils.text import slugify
import requests

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата проведения")
    start_time = models.TimeField(verbose_name="Время начала", default="09:00")
    end_time = models.TimeField(verbose_name="Время окончания", default="12:00")
    description = models.TextField(verbose_name="Описание")
    goals = models.TextField(verbose_name="Цели мероприятия")
    location = models.CharField(max_length=100, verbose_name="Локация", default="Не указан")
    address = models.CharField(max_length=200, verbose_name="Адрес", default="Не указан")
    main_image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name="Главное изображение")
    additional_info = models.TextField(blank=True, verbose_name="Дополнительная информация")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")

    def save(self, *args, **kwargs):
        # Геокодирование адреса с помощью Yandex Geocoder API
        if self.address and (not self.latitude or not self.longitude):
            try:
                api_key = "YOUR_YANDEX_API_KEY"  # Замени на свой API-ключ
                url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={self.address}&format=json"
                response = requests.get(url)
                data = response.json()
                pos = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
                longitude, latitude = map(float, pos.split())
                self.latitude = latitude
                self.longitude = longitude
            except Exception as e:
                print(f"Ошибка геокодирования: {e}")
                self.latitude = None
                self.longitude = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos', verbose_name="Мероприятие")
    image = models.ImageField(upload_to='event_photos/', verbose_name="Фотография")

    def __str__(self):
        return f"Фото для {self.event.title}"

    class Meta:
        verbose_name = "Фотография мероприятия"
        verbose_name_plural = "Фотографии мероприятия"

class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videos', verbose_name="Мероприятие")
    title = models.CharField(max_length=200, verbose_name="Название видео")
    video_file = models.FileField(upload_to='event_videos/', verbose_name="Видео файл")

    def __str__(self):
        return f"{self.title} ({self.event.title})"

    class Meta:
        verbose_name = "Видео мероприятия"
        verbose_name_plural = "Видео мероприятия"

class EventActivity(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='activities', verbose_name="Мероприятие")
    title = models.CharField(max_length=200, verbose_name="Название активности")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=100, verbose_name="Локация", default="Не указан")

    def __str__(self):
        return f"{self.title} ({self.event.title})"

    class Meta:
        verbose_name = "Активность мероприятия"
        verbose_name_plural = "Активности мероприятия"

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

class Conference(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название конференции")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-имя (slug)", help_text="Уникальное имя для URL, например, 'tech-conf-2025'")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    organizers = models.TextField(verbose_name="Организаторы", help_text="Укажите организаторов через запятую")
    format = models.CharField(max_length=100, verbose_name="Формат проведения", help_text="Например: Офлайн, Онлайн, Гибридный")
    goal_image = models.ImageField(upload_to='conference_goals/', verbose_name="Изображение для цели конференции")
    goal_text = models.TextField(verbose_name="Цель конференции")
    plan = models.TextField(verbose_name="План проведения конференции")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"

class ConferenceEvent(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='events', verbose_name="Конференция")
    title = models.CharField(max_length=200, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата проведения")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    format = models.CharField(max_length=100, verbose_name="Формат проведения", help_text="Например: Офлайн (адрес, аудитория) или Онлайн")
    online_link = models.URLField(blank=True, null=True, verbose_name="Ссылка для онлайн-участия")

    def __str__(self):
        return f"{self.title} ({self.conference.title})"

    class Meta:
        verbose_name = "Мероприятие конференции"
        verbose_name_plural = "Мероприятия конференции"

class Speaker(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='speakers', verbose_name="Конференция")
    name = models.CharField(max_length=100, verbose_name="Имя спикера")
    bio = models.TextField(verbose_name="Биография")
    photo = models.ImageField(upload_to='speakers/', verbose_name="Фото спикера")

    def __str__(self):
        return f"{self.name} ({self.conference.title})"

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"

class ConferencePhoto(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='photos', verbose_name="Конференция")
    image = models.ImageField(upload_to='conference_photos/', verbose_name="Фотография")

    def __str__(self):
        return f"Фото для {self.conference.title}"

    class Meta:
        verbose_name = "Фотография конференции"
        verbose_name_plural = "Фотографии конференции"

class ConferenceVideo(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='videos', verbose_name="Конференция")
    title = models.CharField(max_length=200, verbose_name="Название видео")
    video_file = models.FileField(upload_to='conference_videos/', verbose_name="Видео файл")

    def __str__(self):
        return f"{self.title} ({self.conference.title})"

    class Meta:
        verbose_name = "Видео конференции"
        verbose_name_plural = "Видео конференции"