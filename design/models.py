from django.db import models

# Create your models here.
class Photos(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    image=models.ImageField()
    title=models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    price=models.CharField(max_length=250)
    Sales=models.BooleanField(default=False)