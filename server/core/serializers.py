

from rest_framework import serializers
from .models import MapPoint
class MapPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = ('name','lat','lng',)