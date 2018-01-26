from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^location/(?P<location_id>[0-9]+)/$', views.location_info, name='location'),
    url(r'^list/location/$', views.list_locations, name='listlocation'),
    url(r'^crop/(?P<crop_id>[0-9]+)/$', views.crop_info, name='crop'),
    url(r'^device/(?P<device_id>[0-9]+)/$', views.device_info, name='device'),
    url(r'^list/crop/$', views.list_crops, name='listcrop'),
]
