"""
App entity
"""
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customers_created_by"
    )
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customers_modified_by"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
