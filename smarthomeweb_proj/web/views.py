from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Sensor, Werte
from web.forms.TempsFilterForm import TempsFilterForm
from web.forms.HumidsFilterForm import HumidsFilterForm
from web.forms.SensorCreateEditModelForm import SensorCreateEditModelForm
from django.db.models import Max, Min
from datetime import datetime, timedelta


def index(request):
    # return HttpResponse("Hello, world. You're at the web app.")
    return render(request, 'web/index.html')


def tempdetails(request, temp_id):
    print(temp_id + "tempdetails")
    queryset = Sensor.objects.get(pk=temp_id)
    return HttpResponse(f"""Tempdetails for Sensor-ID {temp_id}:
                         {queryset.sen_raum}, 
                         {queryset.sen_ip},
                         {queryset.sen_code}""")

def display_sensors(request):
    sensors = Sensor.objects.all()
    sensorsList = list(sensors)
    if request.method == 'POST':
        form = SensorCreateEditModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SensorCreateEditModelForm()
    return render(request, 'web/sensors.html', {"title":"Sensors",'sensors': sensorsList, 'form': form})
def display_showpress(request):
    queryset = Werte.objects.all()
    pressList = list(queryset)
    return render(request, "web/press.html", {"title":"Press", "pressList": pressList})
    
def pressdetails(request,press_id):
    print(press_id + "Press Details")
    queryset = Sensor.objects.get(pk=press_id)
    return HttpResponse(f"""Press Details for Sensor-ID {press_id}:
                         {queryset.sen_raum}, 
                         {queryset.sen_ip},
                         {queryset.sen_code}""")
def display_humid(request):
    form = HumidsFilterForm()
    form.lowerVal = 4
    queryset = Werte.objects.all()
    humidslist = list(queryset)
    return render(request, "web/humids.html", {"title":"Humids","form": form, "humidslist": humidslist})
def humiddetails(request,humid_id):
    print(humid_id + "Humid Details")
    queryset = Sensor.objects.get(pk=humid_id)
    return HttpResponse(f"""Humid Details for Sensor-ID {humid_id}:
                         {queryset.sen_raum}, 
                         {queryset.sen_ip},
                         {queryset.sen_code}""")
def display_temps(request):
    print("display_temps")
    if request.method == "POST":
        form = TempsFilterForm(request.POST)
        print("display_temps")
        print(form)

        if form.is_valid():
            print(form.cleaned_data)
            lowerVal = form.cleaned_data["lowerVal"]
            if lowerVal is None:
                lowerVal = Werte.objects.aggregate(Min('temperatur'))["temperatur__min"]
                print(lowerVal)
            
            upperVal = form.cleaned_data["upperVal"]
            if upperVal is None:
                upperVal = Werte.objects.aggregate(Max('temperatur'))["temperatur__max"]
                print(upperVal)
                        
            # if upperVal is None:
                # upperVal = Werte.ob
            vonDate = form.cleaned_data["vonDate"]
            bisDate = form.cleaned_data["bisDate"]
            print(f"{lowerVal}, {upperVal}, {vonDate}, {bisDate}")
            # queryset = Werte.objects.filter(temperatur__lte = form.cleaned_data["upperVal"])
            # queryset = Werte.objects.filter(temperatur__range = (lowerVal, upperVal))
            queryset = Werte.objects.filter(datum__gte = vonDate, datum__lte = (bisDate + timedelta(days=1)),
                                            temperatur__lte = upperVal, temperatur__gte = lowerVal)
            
            
            return render(request, "web/temps.html", {"name": "Berg", "tempslist": list(queryset), "form": form})
        else:
            return HttpResponse(f"Error! {form.errors}")
    else:
        print("GET")
        form = TempsFilterForm()
        form.lowerVal = 4
        queryset = Werte.objects.all()
        tempListe = list(queryset)
        #print(dict(queryset))
        return render(request, "web/temps.html", {"title":"Temps","form": form, "tempslist": tempListe})
