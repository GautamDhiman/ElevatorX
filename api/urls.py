from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import ElevatorSystemViewSet

router = DefaultRouter()
router.register(r'elevator-systems', ElevatorSystemViewSet)

urlpatterns = [
    path('elevator-systems/<str:system_name>/', ElevatorSystemViewSet.as_view({'get': 'by_system_name'}),
         name='elevator-systems-by-name'),
    path('', include(router.urls)),
]
