from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("showtemps/", views.display_temps),
    path("showtemps/<str:temp_id>/", views.tempdetails, name="temp_detail"),
    path("showpress/", views.display_press),
    
]