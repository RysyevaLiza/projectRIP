from django.contrib import admin
from django.urls import path

from lab_bmstu import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.start),

    path('tour/', views.GetTours),

    path('tour/<int:id>/', views.GetTour, name='tour_url'),

   # path('countries/', views.GetCountries, name='country_type_url'),

    path('hotel/', views.GetHotels, name='hotel_type_url'),

    path('hotel/<int:id>/', views.GetRooms, name='hotel_url'),

    path('contact/', views.GetContact, name='cont_type_url'),

   # path('countries/<int:id>/', views.GetCountries, name='country_url'),

    path('contact/<int:id>/', views.GetContact, name='count_url'),
]
