from rest_framework import serializers
from hoteldemo.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields=['hotelId','name','location']
