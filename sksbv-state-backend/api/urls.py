from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CircularViewSet, GalleryViewSet, LeaderViewSet, NotificationViewSet, login

router = DefaultRouter()
router.register(r'circular', CircularViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='api-login'),
]
