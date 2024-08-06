from api.models import Customer
from api.serializers import CustomerSerializer
from rest_framework import permissions
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
