from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='image', blank=True)
    title =  models.CharField(max_length=255)
    content = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name