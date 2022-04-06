from django.db import models

# Create your models here.
class MapArea(models.Model):
    name = models.CharField(max_length=254, unique=True)
    
    pass
class MapPoint(models.Model):
    name = models.CharField(max_length=254, unique=True)
    lat = models.DecimalField('Latitude', max_digits=10, decimal_places=8)
    lng = models.DecimalField('Longitude', max_digits=11, decimal_places=8)
    area = models.ForeignKey(to=MapArea, null=True, on_delete=models.SET_NULL)
    
