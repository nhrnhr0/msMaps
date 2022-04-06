from django.contrib import admin
from .models import MapArea, MapPoint
# Register your models here.
class AdminMapArea(admin.ModelAdmin):
    list_display = ('id', 'name',)
    pass
admin.site.register(MapArea, AdminMapArea)

class AdminMapPoint(admin.ModelAdmin):
    list_display = ('id', 'name', 'lat', 'lng', 'area')
    pass
admin.site.register(MapPoint,AdminMapPoint)