from django.contrib import admin
from hotel import views as hotel_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hotel', hotel_views.hotelViewSet)
router.register(r'room', hotel_views.roomViewSet)
router.register(r'show', hotel_views.showlViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
