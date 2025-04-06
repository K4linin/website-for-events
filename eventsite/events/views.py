from django.shortcuts import render
from .models import Event

def index(request):
    events = Event.objects.all().order_by('date')[:3]  # Ближайшие 3 события, сортировка по дате
    return render(request, 'events/index.html', {'events': events})

def events_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def contact(request):
    return render(request, 'events/contact.html')