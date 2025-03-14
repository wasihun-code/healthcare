from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from django.shortcuts import get_object_or_404

from api.serializers import PatientSerializer, DoctorSerializer, DoctorPatientMappingSerializer, RegisterSerializer
from api.models import Patient, Doctor, DoctorPatientMapping


class DoctorListViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message" : f"Doctor {instance.first_name} {instance.first_name} was deleted successfully"},
            status=status.HTTP_200_OK
        )

class PatientListViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message" : f"Patient {instance.first_name} {instance.first_name} was deleted successfully"},
            status=status.HTTP_200_OK
        )


class DoctorPatientMappingViewSet(ModelViewSet):
    queryset = DoctorPatientMapping.objects.all()
    serializer_class = DoctorPatientMappingSerializer


class PatientDoctorsList(ViewSet):
    def list(self, request, patient_id=None):
        if not patient_id:
            return Response({'error': 'Patient Id is required to list all the doctors a specific patient is assigned'})

        patient = get_object_or_404(Patient, pk=patient_id)
        mappings = DoctorPatientMapping.objects.filter(patient=patient)
        doctors = [mapping.doctor for mapping in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]