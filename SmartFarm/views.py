from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import account.views

# Create your views here.
from SmartFarm.models import Location, Crop


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def location_info(request, location_id):
    l = Location.objects.get(id=location_id)

    return JsonResponse({"Latitude": l.lat, "Longitude": l.lon, "Name": l.name})


def list_locations(request):
    list_loc = Location.objects.all()

    response_data = []

    for i in range(len(list_loc)):
        response_data.append({'Latitude': list_loc[i].lat, 'Longitude': list_loc[i].lon, 'Name': list_loc[i].name})

    return JsonResponse(response_data, safe=False)


def crop_info(request, crop_id):
    crop = Crop.objects.get(id=crop_id)

    return JsonResponse({"Name": crop.name, "Location": crop.location.name, "Description": crop.description,
                         "Soil Moisture": crop.soil_moisture})


def list_crops(request):
    list_crop = Crop.objects.all()

    response_data = []

    for i in range(len(list_crop)):
        response_data.append({"Name": list_crop[i].name, "Location": list_crop[i].location.name,
                              "Description": list_crop[i].description, "Soil Moisture": list_crop[i].soil_moisture})

    return JsonResponse(response_data, safe=False)


def device_info(request, device_id):
    device = Crop.objects.get(id=device_id)

    return JsonResponse({"Device Name": device.name, "Crop": device.crop.name})
