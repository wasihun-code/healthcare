from rest_framework.serializers import ModelSerializer
from api.models import Patient, Doctor, DoctorPatientMapping
from rest_framework import serializers
from django.contrib.auth.models import User

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_email(self, value):
        instance = self.instance  # Get the current patient instance
        if instance and instance.email == value:
            return value

        if Patient.objects.filter(email=value).exists():
            raise serializers.ValidationError('Patient with this email already exists')
        return value


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorPatientMappingSerializer(ModelSerializer):
    class Meta:
        model = DoctorPatientMapping
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

