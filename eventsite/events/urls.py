from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events_list, name='events_list'),
    path('contact/', views.contact, name='contact'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]