from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientAddressViewSet
from .views import ProfessionalViewSet, ProfessionalAddressViewSet
from .views import AppointmentViewSet
from .views import ClientAppointmentViewSet, ProfessionalAppointmentViewSet
from .views import AvailabilityViewSet, ProfessionViewSet, QualificationViewSet
from .views import ServiceViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'professionals', ProfessionalViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'profession', ProfessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Clients specific routes
    path('clients/', ClientViewSet.as_view({'get': 'list'}), name='client-list'),
    path('register/clients/', ClientViewSet.as_view({'post': 'create'}), name='register-client'),
    path('clients/<slug:slug>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-detail'),
    path('clients/<slug:slug>/address/', ClientAddressViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='client-address-list'),
    path('clients/<slug:slug>/address/<slug:address_slug>/', ClientAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-address-detail'),
    #Professionals specific routes
    path('professionals/', ProfessionalViewSet.as_view({'get': 'list'}), name='professional-list'),
    path('register/professionals/', ProfessionalViewSet.as_view({'post': 'create'}), name='register-professional'),
    path('professionals/<slug:slug>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-detail'),
    path('professionals/<slug:slug>/address/', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='professional-address-list'),
    path('professionals/<slug:slug>/address/<slug:address_slug>/', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-address-detail'),
    #Appointments specific routes
    path('appointments/', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='appointment-list'),
    path('appointments/<slug:appointment_slug>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='appointment-detail'),
    path('clients/<slug:slug>/appointments/', ClientAppointmentViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='client-appointment-list'),
    path('clients/<slug:slug>/appointments/<slug:appointment_slug>/', ClientAppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-appointment-detail'),
    path('professionals/<slug:slug>/appointments/', ProfessionalAppointmentViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='professional-appointment-list'),
    #Availabilities specific routes
    path('availabilities/', AvailabilityViewSet.as_view({'get': 'list'}), name='admin-availability-list'),
    path('professionals/<slug:slug>/availabilities/', AvailabilityViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='availability-list'),
    path('professionals/<slug:slug>/availabilities/<slug:availability_slug>/', AvailabilityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='availability-detail'),
    #Professions specific routes
    path('professions/', ProfessionViewSet.as_view({'get': 'list', 'post': 'create'}), name='profession-list'),
    path('professionals/<slug:slug>/professions/', ProfessionViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='professional-profession-list'),
    #Qulifications specific routes
    path('qualifications/', QualificationViewSet.as_view({'get': 'list'}), name="qualifications-list"),
    path('professionals/<slug:slug>/qualifications/', QualificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='professional-qualifications-list'),
    path('professionals/<slug:slug>/qualifications/<slug:qualification_slug>', QualificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-qualification-detail'),
    #Services specific routes
    path('services/', ServiceViewSet.as_view({'get': 'list'}), name="service-list"),
    path('professionals/<slug:slug>/services/', ServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name="professional-service-list"),
    path('professionals/<slug:slug>/services/<slug:service_slug>/', ServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-service-detail')
]
