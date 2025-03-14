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


class PatientListViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorPatientMappingViewSet(ModelViewSet):
    queryset = DoctorPatientMapping.objects.all()
    serializer_class = DoctorPatientMappingSerializer


class PatientDoctorsList(ViewSet):
    def list(self, request, patient_id=None):
        patient = get_object_or_404(Patient, pk=patient_id)
        mappings = DoctorPatientMapping.objects.filter(patient=patient)
        doctors = [mapping.doctor for mapping in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]