from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'vehicle',views.VehicleViewSet)

urlpatterns=[
    path('', include(router.urls))
]