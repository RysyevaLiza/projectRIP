from django.contrib import admin
from django.urls import path, include
from lab_bmstu import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'pages', views.hotelViewSet)
#router.register(r'room', hotel_views.roomViewSet)
#router.register(r'show', hotel_views.showlViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')),

    path('', views.start),

    path('tour/', views.GetTours),

    path('tour/<int:id>/', views.GetTour, name='tour_url'),

   # path('countries/', views.GetCountries, name='country_type_url'),

    path('hotel/', views.GetHotels, name='hotel_type_url'),

    path('hotel/<int:id>/', views.GetRooms, name='hotel_url'),

    path('contact/', views.GetContact, name='cont_type_url'),

   # path('countries/<int:id>/', views.GetCountries, name='country_url'),

    path('contact/<int:id>/', views.GetContact, name='count_url'),
    path('',include(router.urls))
]
