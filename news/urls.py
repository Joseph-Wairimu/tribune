from django.urls import path,register_converter

from . import views
from .models import UrlDateConverter
register_converter(UrlDateConverter,'date')
urlpatterns=[
    path('hello/',views.welcome,name = 'welcome'),
    path('today/',views.news_of_day,name='newsToday'),
    path('archives/<date:past_date>/',views.past_days_news,name = 'pastNews')
]
