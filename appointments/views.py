from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .serializers.appointment_serializers import AppointmentSerializer
from .models import Appointment


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['appointment_occasion', 'status',]
