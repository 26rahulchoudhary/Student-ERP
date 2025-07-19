from django.db import models
from django.conf import settings

# Create your models here.

class FacultyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"{self.user.username} ({self.department})"
