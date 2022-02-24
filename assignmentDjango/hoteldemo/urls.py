from django.urls import path
from . import views

urlpatterns= [
   # path("home/", views.home, name="home"),
    path("listhotels/", views.listHotels, name="listhotels"),
    path("hoteldetail/<int:hotelid>", views.hotel_detail, name="hoteldetail"),
    path("hotels/", views.HotelList.as_view())


]