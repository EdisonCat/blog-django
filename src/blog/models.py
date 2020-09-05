from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=False)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={'pk': self.id})

    def get_absolute_url_delete (self):
        return reverse("blog:article_delete", kwargs={'pk': self.id})
