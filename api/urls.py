from django.urls import  path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (
    DoctorListViewSet,
    PatientListViewSet,
    DoctorPatientMappingViewSet,
    PatientDoctorsList, RegisterViewSet
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterViewSet.as_view(), name='register'),


    path('doctors/', DoctorListViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='doctor-list'),
    path('doctors/<int:pk>',DoctorListViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='single-doctor'),

    path('patients/', PatientListViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='patients-list'),
    path('patients/<int:pk>/', PatientListViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='single-patient'),

    path('mappings/', DoctorPatientMappingViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='mapping-list'),
    path('mappings/<int:pk>/delete/', DoctorPatientMappingViewSet.as_view({
        'delete': 'destroy'
    }), name='delete-mapping'),
    path('mappings/<int:patient_id>/', PatientDoctorsList.as_view({
        'get': 'list'
    }), name='patient-doctors'),
]