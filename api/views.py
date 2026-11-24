from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Circular, Gallery, Leader, Notification, DistrictLeader, WorkingCommittee
from .serializers import (
    CircularSerializer,
    GallerySerializer,
    LeaderSerializer,
    NotificationSerializer,
    DistrictLeaderSerializer,
    WorkingCommitteeSerializer,
)

class CircularViewSet(viewsets.ModelViewSet):
    queryset = Circular.objects.all().order_by('-created_at')
    serializer_class = CircularSerializer
    search_fields = ['title', 'description']
    filterset_fields = ['created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer
    search_fields = ['title']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class LeaderViewSet(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    search_fields = ['name', 'designation']
    filterset_fields = ['designation']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    search_fields = ['title', 'message']
    filterset_fields = ['created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class DistrictLeaderViewSet(viewsets.ModelViewSet):
    queryset = DistrictLeader.objects.all()
    serializer_class = DistrictLeaderSerializer
    search_fields = ['name', 'designation', 'district']
    filterset_fields = ['designation', 'district']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class WorkingCommitteeViewSet(viewsets.ModelViewSet):
    queryset = WorkingCommittee.objects.all()
    serializer_class = WorkingCommitteeSerializer
    search_fields = ['name', 'designation', 'district']
    filterset_fields = ['designation', 'district']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]


@api_view(['POST'])
def login(request):
    """
    Login endpoint for admin authentication.
    Expects: {"username": "admin", "password": "admin123456"}
    Returns: {"token": "YOUR_TOKEN_HERE", "user": {"id": 1, "username": "admin", "email": "admin@example.com"}}
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'Username and password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)