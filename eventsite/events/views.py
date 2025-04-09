from django.shortcuts import render, get_object_or_404
from .models import Event, Partner, Video, News, Conference
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

def index(request):
    # Получаем все мероприятия
    events = Event.objects.all().order_by('date')

    # Фильтр по дате
    date_filter = request.GET.get('date')
    if date_filter:
        try:
            filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            events = events.filter(date=filter_date)
        except ValueError:
            pass

    # Фильтр по локации
    location_filter = request.GET.get('location')
    if location_filter:
        events = events.filter(location__icontains=location_filter)

    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        events = events.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    # Пагинация
    paginator = Paginator(events, 5)  # 5 мероприятий на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Получаем последние 3 мероприятия для секции "Новые мероприятия"
    recent_events = Event.objects.all().order_by('-date')[:3]

    # Получаем партнеров, видео и новости
    partners = Partner.objects.all()
    videos = Video.objects.all()
    news = News.objects.all().order_by('-publication_date')[:3]  # Последние 3 новости

    return render(request, 'events/index.html', {
        'page_obj': page_obj,
        'recent_events': recent_events,
        'search_query': search_query,
        'date_filter': date_filter,
        'location_filter': location_filter,
        'partners': partners,
        'videos': videos,
        'news': news,
    })

def events_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'partners': Partner.objects.all(),  # Общие партнеры
    })

def contact(request):
    return render(request, 'events/contact.html')

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'events/news_detail.html', {'news': news_item})

def news_list(request):
    news = News.objects.all().order_by('-publication_date')
    paginator = Paginator(news, 6)  # 6 новостей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/news_list.html', {'page_obj': page_obj})

def conference_detail(request, slug):
    conference = get_object_or_404(Conference, slug=slug)
    # Сортируем мероприятия по дате и времени
    conference_events = conference.events.all().order_by('date', 'start_time')
    return render(request, 'events/conference_detail.html', {
        'conference': conference,
        'conference_events': conference_events,
        'partners': Partner.objects.all(),  # Общие партнеры
    })