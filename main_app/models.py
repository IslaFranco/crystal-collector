from django.db import models
from django.urls import reverse

# Create your models here.

METHODS = (
    ('S', 'Sunlight'),
    ('M', 'Moonlight'),
    ('W', 'Water'),
    ('I', 'Incense',)
)

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    properties = models.CharField(max_length=100)
    chakras = models.CharField(max_length=100)
    zodiac = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})

class Cleanse(models.Model):   
    date = models.DateField('Cleansing Date')
    method = models.CharField(
        max_length=1, 
        choices=METHODS,
         default='M'
         )

    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)  

    def __str__(self):
        return f'{self.get_method_display()} on {self.date}'   
        # Moonlight on 09-23-2022 
        # 

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=5000) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_id': self.id})    



#Anytime you mkae changes to our models, we need to make migrations to represent your data to your database
        
