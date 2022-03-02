# Rest Application Using the Django Framework
--------
Set Up
--------
I have used tunnel from dev.cs.smu.ca and used the database since dev.cs.smu.ca mysql instance  was not accebile from local machine.
Install below library..

1. $ pip install django
2. $ pip install django_rest_framework
3. $ pip install pymysql
4. $ pip install django-rest-swagger


-----------------------
About The Application
-----------------------
This application uses Django framework for developing the resp api for getting and creating the entries in the hotel details tables.
All the endpoints are listed into one page http://127.0.0.1:8000/swagger-ui/.
Sample object for hotel 
{
    "hotelId": int,
    "name": STRING,
    "location": String 
    }
Function bases views 
1. GET:  http://127.0.0.1:8000/app/listhotels/ To get the list of hotels saved in the database table.
2. POST:  http://127.0.0.1:8000/app/listhotels/  with request body as hotel object to create a new hotel in database.
3. GET : http://127.0.0.1:8000/app/hoteldetail/{hotelid} To get the detail of a particular hotel by using primary key hotel id.
4. PUT:  http://127.0.0.1:8000/app/hoteldetail/{hotelid} to update the hotel details with hotel id and request body as hotel object.
5. DELETE :   http://127.0.0.1:8000/app/hoteldetail/{hotelid} to delete the hotel from the database.
 
  
