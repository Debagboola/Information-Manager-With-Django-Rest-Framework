from datetime import datetime

from django.db import models


# Create your models here.

class Info(models.Model):
    GENDER = [
        ('male', 'male'),
        ('female', 'female')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(unique=True, blank=True, )
    gender = models.CharField(choices=GENDER, default='male', blank=True, max_length=10)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
