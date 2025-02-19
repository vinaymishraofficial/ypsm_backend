from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import GallerySitemap
from . import views

sitemaps = {
    'gallery': GallerySitemap,
}

urlpatterns = [
    path('gallery/<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap-index.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap-index'),
]
