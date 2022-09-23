from django.db import models

# Create your models here.

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    properties = models.CharField(max_length=100)
    chakras = models.CharField(max_length=100)
    zodiac = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Anytime you mkae changes to our models, we need to make migrations to represent your data to your database
        
