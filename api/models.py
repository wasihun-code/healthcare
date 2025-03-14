from django.core.validators import EmailValidator
from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=[('M', 'Male'), ('F', 'Female')])
    email = models.EmailField(validators=[EmailValidator()])
    current_medications = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


specialization_choices = [
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Neurology', 'Neurology'),
    ('Orthopedics', 'Orthopedics'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry', 'Psychiatry'),
    ('Radiology', 'Radiology'),
    ('General Medicine', 'General Medicine'),
]


class Doctor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100, choices=specialization_choices, blank=True, null=True)
    license_number = models.CharField(max_length=100, unique=True)
