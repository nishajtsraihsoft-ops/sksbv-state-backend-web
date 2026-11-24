from rest_framework import serializers
from .models import Circular, Gallery, Leader, Notification, DistrictLeader, WorkingCommittee

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

class DistrictLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictLeader
        fields = '__all__'

class WorkingCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingCommittee
        fields = '__all__'

