from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Products.Status.Published)
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Products(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    image = models.ImageField(upload_to='products/images')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE
                                 )
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )
    objects = models.Manager() # default manager
    published = PublishedManager


    class Meta:
        ordering = ["-publish_time"]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products_detail_page", args=[self.slug])






