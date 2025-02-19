from django.db import models
from tinymce.models import HTMLField # type: ignore

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    Description = HTMLField()
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
