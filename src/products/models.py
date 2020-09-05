from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField()
    featured = models.BooleanField(default=True)

    def get_absolute_url_detail(self):
        # return f'/products/{self.id}/'
        return reverse("products:products_detail", kwargs={"my_id": self.id})

    def get_absolute_url_delete(self):
        return reverse("products:products_delete", kwargs={"my_id": self.id})

