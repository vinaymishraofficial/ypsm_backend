from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.categoryName

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.FileField(upload_to='gallery/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
