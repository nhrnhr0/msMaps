

from rest_framework import serializers
from .models import MapPoint
class MapPointSerializer(serializers.ModelSerializer):
    marker = serializers.CharField(source='area.markerUrl', read_only=True)
    class Meta:
        model = MapPoint
        fields = ('name','lat','lng', 'marker')