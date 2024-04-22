from django.db import models

# Create your models here.

class Finch(models.Model):
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    
    def __str__(self):
        return self.common_name
