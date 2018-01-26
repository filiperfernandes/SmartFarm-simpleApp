from django.db import models

# Create your models here.


class Location(models.Model):
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    soil_moisture = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
