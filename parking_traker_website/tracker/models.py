from django.db import models

# Create your models here.
class Car_Count(models.Model):
    time = models.CharField(max_length = 10)
    count = models.IntegerField()