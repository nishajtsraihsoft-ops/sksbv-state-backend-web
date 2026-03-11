from rest_framework import serializers
from .models import Circular, Gallery, Leader, Notification

class CircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circular
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
