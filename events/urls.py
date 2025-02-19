from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import EventSitemap
from . import views

sitemaps = {
    'events': EventSitemap,
}

urlpatterns = [
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap-index.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap-index'),
]