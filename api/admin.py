from django.contrib import admin

from api.models import Patient, Doctor

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
