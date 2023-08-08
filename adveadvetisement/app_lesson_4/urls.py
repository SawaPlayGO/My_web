from django.urls import path
from .views import marmelads, top_sellers, logining


urlpatterns = [
    path('marmelads/', marmelads, name='marmelads'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('logining/', logining, name='logining')
]
