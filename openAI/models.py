from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    getUser = models.ForeignKey(User, on_delete=models.CASCADE)
    getLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    getLongitude = models.DecimalField(max_digits=9, decimal_places=6)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.getUser.username}'s Location"