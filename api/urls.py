from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import ElevatorSystemViewSet, ElevatorRequestViewSet, ElevatorViewSet

router = DefaultRouter()
router.register(r'elevator-systems', ElevatorSystemViewSet)

urlpatterns = [
    path('elevator-systems/<int:elevator_system>/elevators/<int:pk>/requests/',
         ElevatorRequestViewSet.as_view({'get': 'requests_for_elevator'}), name='elevator-requests'),
    path('elevator-systems/<int:elevator_system>/elevators/<int:pk>/next-destination-floor/',
         ElevatorViewSet.as_view({'get': 'next_destination_floor'}), name='next-destination-floor'),
    path('elevator-systems/<str:system_name>/', ElevatorSystemViewSet.as_view({'get': 'by_system_name'}),
         name='elevator-systems-by-name'),
    path('elevator-systems/<int:pk>/create-elevator-request',
         ElevatorSystemViewSet.as_view({'post': 'request_elevator'}), name='create-elevator-request'),
    path('', include(router.urls)),
]
