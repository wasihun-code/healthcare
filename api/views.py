from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import PatientSerializer, DoctorSerializer
from api.models import Patient, Doctor

# Create your views here.


class DoctorListViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientListViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

