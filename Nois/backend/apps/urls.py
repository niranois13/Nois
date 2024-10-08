from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.client_views import ClientViewSet, ClientAddressViewSet
from .views.professional_views import ProfessionalViewSet, ProfessionalAddressViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'professionals', ProfessionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Clients specific routes
    path('register/clients/', ClientViewSet.as_view({'post': 'create'}), name='register-client'),
    path('clients/<slug:slug>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-detail'),
    path('clients/<slug:slug>/address/', ClientAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='client-address-list'),
    path('clients/<slug:slug>/address/<slug:address_slug>', ClientAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='client-address-detail'),
    #Professionals specific routes
    path('register/professionals/', ProfessionalViewSet.as_view({'post': 'create'}), name='register-professional'),
    path('professionals/<slug:slug>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-detail'),
    path('professionals/<slug:slug>/address/', ProfessionalAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='professional-address-list'),
    path('professionals/<slug:slug>/address/<slug:address_slug>', ProfessionalAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='professional-address-detail'),
]
