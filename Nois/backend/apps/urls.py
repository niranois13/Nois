from django.urls import path
from .views import (
    UserViewSet,
    ClientViewSet, ClientAddressViewSet,
    ProfessionalViewSet, ProfessionalAddressViewSet,
    AppointmentViewSet, ClientAppointmentViewSet, ProfessionalAppointmentViewSet,
    AvailabilityViewSet, QualificationViewSet,
    ServiceViewSet, ProfessionalServiceViewSet, SearchView
)

urlpatterns = [
    #Clients specific routes
    path('api/clients/', ClientViewSet.as_view({'get': 'list'}), name='client-list'),
    path('api/register/clients/', ClientViewSet.as_view({'post': 'create'}), name='register-client'),
    path('api/clients/<slug:slug>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-detail'),
    path('api/clients/<slug:slug>/address/', ClientAddressViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='client-address-list'),
    path('api/clients/<slug:slug>/address/<slug:address_slug>/', ClientAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-address-detail'),
    #Professionals specific routes
    path('api/professionals/', ProfessionalViewSet.as_view({'get': 'list'}), name='professional-list'),
    path('api/register/professionals/', ProfessionalViewSet.as_view({'post': 'create'}), name='register-professional'),
    path('api/professionals/<slug:slug>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='professional-detail'),
    path('api/professionals/<slug:slug>/address/', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='professional-address-list'),
    path('api/professionals/<slug:slug>/address/<slug:address_slug>/', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-address-detail'),
    #Appointments specific routes
    path('api/appointments/', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='appointment-list'),
    path('api/appointments/<slug:appointment_slug>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='appointment-detail'),
    path('api/clients/<slug:slug>/appointments/', ClientAppointmentViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='client-appointment-list'),
    path('api/clients/<slug:slug>/appointments/<slug:appointment_slug>/', ClientAppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-appointment-detail'),
    path('api/professionals/<slug:slug>/appointments/', ProfessionalAppointmentViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='professional-appointment-list'),
    #Availabilities specific routes
    path('api/availabilities/', AvailabilityViewSet.as_view({'get': 'list'}), name='admin-availability-list'),
    path('api/professionals/<slug:slug>/availabilities/', AvailabilityViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='availability-list'),
    path('api/professionals/<slug:slug>/availabilities/<slug:availability_slug>/', AvailabilityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='availability-detail'),
    #Qualifications specific routes
    path('api/qualifications/', QualificationViewSet.as_view({'get': 'list'}), name="qualifications-list"),
    path('api/professionals/<slug:slug>/qualifications/', QualificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='professional-qualifications-list'),
    path('api/professionals/<slug:slug>/qualifications/<slug:qualification_slug>', QualificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-qualification-detail'),
    #Public services routes
    path('api/services/', ServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name="service-list"),
    path('api/services/<slug:slug>/', ServiceViewSet.as_view({'get': 'retrieve'}), name="service-detail"),
    #Professional services specific routes
    path('api/professionals/<slug:professional_slug>/services/', ProfessionalServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name="professional-service-list"),
    path('api/professionals/<slug:professional_slug>/services/<slug:service_slug>/', ProfessionalServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-service-detail'),
    #Search routes
    path('api/search/', SearchView.as_view(), name='search'),
    path('api/users/get_my_slug/', UserViewSet.as_view({'get': 'get_my_slug'}), name="user-slug"),
    path('api/users/check-auth/', UserViewSet.as_view({'get': 'check_auth_status'}), name="user-slug"),
]
