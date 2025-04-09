from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events_list, name='events_list'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),  # Изменён маршрут
    path('contact/', views.contact, name='contact'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/', views.news_list, name='news_list'),
    path('conference/<slug:slug>/', views.conference_detail, name='conference_detail'),
]