from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .serializers.patient_serializers import PatientSerializer
from .serializers.dentist_serializers import DentistSerializer

from .models import Patient, Dentist


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class DentistViewSet(ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    permission_classes = {IsAuthenticated}
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
