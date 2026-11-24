from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CircularViewSet,
    GalleryViewSet,
    LeaderViewSet,
    NotificationViewSet,
    DistrictLeaderViewSet,
    WorkingCommitteeViewSet,
    login,
)

router = DefaultRouter()
router.register(r'circular', CircularViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'district-leaders', DistrictLeaderViewSet, basename='district-leader')
router.register(r'district_leaders', DistrictLeaderViewSet, basename='district_leader')
router.register(r'working-committee', WorkingCommitteeViewSet, basename='working-committee')
router.register(r'working_committee', WorkingCommitteeViewSet, basename='working_committee')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='api-login'),
]

