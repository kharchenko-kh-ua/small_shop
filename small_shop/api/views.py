"""
API viewsets
"""
from api.models import Customer
from api.serializers import CustomerSerializer
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)
