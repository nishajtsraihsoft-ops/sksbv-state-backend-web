from django.db import models

class Circular(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='circulars/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Leader(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='leaders/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
