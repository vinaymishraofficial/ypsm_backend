from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from events.sitemaps import EventSitemap
from gallery.sitemaps import GallerySitemap
from django.views.generic import TemplateView

sitemaps = {
    'events': EventSitemap,
    'gallery': GallerySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('', include('teachers.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include('contacts.urls')),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap-index.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap-index'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
