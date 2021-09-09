from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from photos.views import PhotoViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'photos', PhotoViewSet) #register "/photos" routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]