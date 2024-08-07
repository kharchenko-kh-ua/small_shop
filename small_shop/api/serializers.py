"""
API serializers
"""
from api.models import Customer
from django.contrib.auth.models import User
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "photo")

    def create(self, validated_data):
        return Customer.objects.create(
            created_by=self.context["request"].user,
            modified_by=self.context["request"].user,
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.modified_by = self.context["request"].user
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
