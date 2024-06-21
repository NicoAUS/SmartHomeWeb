from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("showtemps/", views.display_temps),
    path("showtemps/<str:temp_id>/", views.tempdetails, name="temp_detail"),
    path("showhumid/", views.display_humid),
    path("showhumid/<str:humid_id>/", views.humiddetails, name="humid_detail"),
    path("sensors/", views.display_sensors,  name='sensor_form'),
    path("showpress/", views.display_showpress,  name='press_detail'),
    path("showpress/<str:press_id>/", views.pressdetails, name="press_detail"),
    
    
]