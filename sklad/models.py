from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 256)
    price = models.IntegerField()
    img_path = models.CharField(max_length = 512)
    about =  models.TextField()