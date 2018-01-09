from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumb = models.ImageField(default='default.png', blank=True)
    # author later

    # string representation
    def __str__(self):
        return self.title
