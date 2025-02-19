from django.db import models
from tinymce.models import HTMLField # type: ignore

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Event(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = HTMLField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title