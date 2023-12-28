from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    hero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
