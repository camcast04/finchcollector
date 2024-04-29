from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    
    def __str__(self):
        return self.common_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id':self.id})