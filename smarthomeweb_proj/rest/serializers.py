from rest_framework import serializers
from .models import Werte, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sen_raum', 'sen_ip']


class WerteSerializer(serializers.ModelSerializer):
   sensor = SensorSerializer()
   class Meta:
        model = Werte
        fields = ['id', 'temperatur', 'sensor']
        #fields = "__all__"


        