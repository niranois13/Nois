from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientAddressViewSet
from .views import ProfessionalViewSet, ProfessionalAddressViewSet
from .views import AppointmentViewSet
from .views import ClientAppointmentViewSet, ProfessionalAppointmentViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'professionals', ProfessionalViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Clients specific routes
    path('clients/', ClientViewSet.as_view({'get': 'list'}), name='client-list'),
    path('register/clients/', ClientViewSet.as_view({'post': 'create'}), name='register-client'),
    path('clients/<slug:slug>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-detail'),
    path('clients/<slug:slug>/address/', ClientAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='client-address-list'),
    path('clients/<slug:slug>/address/<slug:address_slug>/', ClientAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-address-detail'),
    #Professionals specific routes
    path('professionals/', ProfessionalViewSet.as_view({'get': 'list'}), name='professional-list'),
    path('register/professionals/', ProfessionalViewSet.as_view({'post': 'create'}), name='register-professional'),
    path('professionals/<slug:slug>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-detail'),
    path('professionals/<slug:slug>/address/', ProfessionalAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='professional-address-list'),
    path('professionals/<slug:slug>/address/<slug:address_slug>/', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-address-detail'),
    #Appointment specific routes
    path('appointments/', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='appointment-list'),
    path('appointments/<slug:appointment_slug>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='appointment-detail'),
    path('clients/<slug:slug>/appointments/', ClientAppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='client-appointment-list'),
    path('clients/<slug:slug>/appointments/<slug:appointment_slug>/', ClientAppointmentViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'}), name='client-appointment-detail'),
    path('professionals/<slug:slug>/appointments/', ProfessionalAppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='professional-appointment-list'),
    path('professionals/<slug:slug>/appointments/<slug:appointment_slug>/', ProfessionalAppointmentViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'}), name='professional-appointment-detail'),
]
