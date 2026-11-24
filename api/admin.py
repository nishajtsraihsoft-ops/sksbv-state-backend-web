from django.contrib import admin
from .models import Circular, Gallery, Leader, Notification, DistrictLeader, WorkingCommittee

@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(DistrictLeader)
class DistrictLeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'district')
    list_filter = ('district', 'designation')
    search_fields = ('name', 'designation', 'district')

@admin.register(WorkingCommittee)
class WorkingCommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'district')
    list_filter = ('district', 'designation')
    search_fields = ('name', 'designation', 'district')

