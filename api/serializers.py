from rest_framework.serializers import ModelSerializer

from api.models import Patient, Doctor


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


