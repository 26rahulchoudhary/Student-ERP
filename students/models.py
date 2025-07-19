from django.db import models
from django.conf import settings

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    # Add more fields as needed

    def __str__(self):
        return f"{self.user.username} ({self.enrollment_number})"
