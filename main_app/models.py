from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class ShinyObject(models.Model):
  name = models.CharField(max_length=50)
  material = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('shiny_objects_detail', kwargs={'pk': self.id})



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

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1,
                          choices=MEALS,
                          default=MEALS[0][0])
  #creating foreign key
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  class Meta:
    ordering = ['-date']