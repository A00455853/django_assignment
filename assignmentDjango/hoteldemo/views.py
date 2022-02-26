from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from hoteldemo.models import Hotel
from hoteldemo.serializers import HotelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
# creating the http json response
def home(request):
    hotel = {
        'id': 123,
        'name': 'IBIS HOTEL'

    }
    data = Hotel.objects.all();
    response = {'hotels': list(data.values('name', 'location'))}

    return JsonResponse(response)


# function based views
@api_view(['GET', 'POST'])

def listHotels(request):
    """
    Function based views for get and post type of request
    """
    serializer_class = HotelSerializer
    if request.method == 'GET':
        hotels = Hotel.objects.all();
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#primary key based get , put and update opetaion
@api_view(['GET','PUT','DELETE'])
def hotel_detail(request,hotelid):
    try:
        hotel = Hotel.objects.get(hotelId=hotelid)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HotelSerializer(hotel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class based views
class HotelList(APIView):

    def get(self,request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)