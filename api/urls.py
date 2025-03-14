from django.urls import  path

from api.views import (
    DoctorListViewSet,
    PatientListViewSet,
    DoctorPatientMappingViewSet,
    PatientDoctorsList
)

urlpatterns = [
    path('doctors/', DoctorListViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='doctor-list'),
    path('doctors/<int:pk>/',DoctorListViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='single-doctor'),

    path('patients/', PatientListViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='patients-list'),
    path('patients/<int:pk>/', PatientListViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='single-patient'),

    path('mappings/', DoctorPatientMappingViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='mapping-list'),
    path('mappings/<int:patient_id>/', PatientDoctorsList.as_view({
        'get': 'list'
    }), name='patient-doctors'),

    path('mappings/<int:pk>/', DoctorPatientMappingViewSet.as_view({
        'delete': 'destroy'
    }), name='delete-mapping'),

]