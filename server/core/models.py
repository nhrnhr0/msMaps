from ast import Return
from django.db import models

# Create your models here.
class MapArea(models.Model):
    name = models.CharField(max_length=254, unique=True)
    markerUrl = models.CharField(max_length=254, null=True, blank=True)
    def __str__(self):
        return self.name
    pass
class MapPoint(models.Model):
    name = models.CharField(max_length=254, unique=True)
    lat = models.DecimalField('Latitude', max_digits=11, decimal_places=8)
    lng = models.DecimalField('Longitude', max_digits=11, decimal_places=8)
    area = models.ForeignKey(to=MapArea, null=True, blank=True, on_delete=models.SET_NULL)
    
