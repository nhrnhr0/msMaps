from django.http import JsonResponse
from django.shortcuts import redirect, render
import csv
import io

from server.secrects import MAPS_API_KEY
from .models import MapPoint
from django.contrib import messages
from .serializers import MapPointSerializer
def directions_view(request):
    
    return render(request, 'directions.html',context={'MAPS_API_KEY': MAPS_API_KEY})
def get_all_points(request):
    points = MapPoint.objects.all()
    data = MapPointSerializer(points, many=True).data
    context = {'points': data}
    return JsonResponse(context)
# Create your views here.
def admin_load_map_csv(request):
    if request.method == "POST":
        print(request)
        myfile = request.FILES['file']
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        failed = 0
        success = 0
        # Generate a list comprehension
        data = [line for line in reader]
        print(data)
        for entry in data:
            name = entry['name']
            x = entry['x']
            y = entry['y']
            try:
                MapPoint.objects.create(name=name, lat=x, lng=y)
                success += 1
            except:
                failed += 1
        messages.add_message(request, messages.SUCCESS, 'נוספו {} מקומות חדשים'.format(success))
        messages.add_message(request, messages.ERROR, '{} נכשלו'.format(failed))
        return redirect()
    return render(request, 'admin_load_map_csv.html', context={})