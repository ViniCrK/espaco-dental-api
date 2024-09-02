from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers.appointment_serializers import AppointmentSerializer
from .models import Appointment


class AppointmentList(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):
    def get_object(self, id):
        try:
            return Appointment.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        appointment = self.get_object(id)
        serializer = AppointmentSerializer(appointment)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        appointment = self.get_object(id)
        serializer = AppointmentSerializer(appointment, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        appointment = self.get_object(id)
        appointment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
