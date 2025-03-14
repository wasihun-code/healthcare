from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.serializers import PatientSerializer, DoctorSerializer, DoctorPatientMappingSerializer
from api.models import Patient, Doctor, DoctorPatientMapping


# Create your views here.


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
        print(patient)
        mappings = DoctorPatientMapping.objects.filter(patient=patient)
        print(mappings)
        doctors = [mapping.doctor for mapping in mappings]
        print(doctors)
        serializer = DoctorSerializer(doctors, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

