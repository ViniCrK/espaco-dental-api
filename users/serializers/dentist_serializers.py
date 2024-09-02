from rest_framework import serializers
from ..models.dentist import Dentist


class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'
