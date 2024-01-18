# news/urls.py
from django.urls import path
from .views import home_page, news_details

urlpatterns = [
    path('', home_page, name='home-page'),
    path('news/<int:id>/', news_details, name='news-details-page'),
]
