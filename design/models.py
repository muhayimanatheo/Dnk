from django.db import models    
from django.utils import timezone

# Create your models here.
class Photos(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    price=models.CharField(max_length=250)
    Sales=models.BooleanField(default=False)
    




    

   
