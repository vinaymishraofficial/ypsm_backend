from django.contrib.sitemaps import Sitemap
from .models import Gallery

class GallerySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Gallery.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
