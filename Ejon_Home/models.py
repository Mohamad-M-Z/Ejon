from django.db import models

# Create your models here.

class Product(models.Model):

    size = [
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
    ]

    subject = models.CharField(max_length=255, blank=True)
    Photo = models.ImageField(upload_to='image/', blank=True, default='product-1.png')
    content = models.TextField()
    type_product = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    size = models.CharField(max_length=3, choices=size, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name