from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotelId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return  self.hotelId+self.name+self.location