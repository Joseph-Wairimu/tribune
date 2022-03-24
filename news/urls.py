from django.urls import path,register_converter
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .models import UrlDateConverter
register_converter(UrlDateConverter,'date')
urlpatterns=[
    path('',views.news_of_day,name='newsToday'),
    path('archives/<date:past_date>/',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/(\d+)',views.article,name ='article')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
