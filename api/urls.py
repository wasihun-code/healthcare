from django.urls import  path

from api.views import DoctorListViewSet, PatientListViewSet

urlpatterns = [
    path('doctors/', DoctorListViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='doctor-list'),
    path('doctors/<int:pk>/',DoctorListViewSet.as_view({
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
    }), name='single-patients'),
]