from django.urls import path
from . import views

urlpatterns= [
   # path("home/", views.home, name="home"),
    path("listhotels/", views.listHotels, name="listhotels_functionbased_views"),
    path("hoteldetail/<int:hotelid>", views.hotel_detail, name="hoteldetail"),
    path("hotels/", views.HotelList.as_view(), name= "hotels class based views")


]