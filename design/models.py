from django.db import models

# Create your models here.
class Photos(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    price=models.CharField(max_length=250)
    Sales=models.BooleanField(default=False)