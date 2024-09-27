from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClientViewSet, ProfessionalViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'professionals', ProfessionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

'''
urlpatterns = [
    path(
        'register/professional/',
        ProfessionalRegistrationView.as_view(),
        name='register_professional'
        ),
    path(
        'register/client/',
        ClientRegistrationView.as_view(),
        name='register_client'
        ),
    path(
        'api/admin/users/',
        UserListView.as_view(),
        name='admin-user-list'
        ),
    path(
        'api/admin/professionals/',
        ProfessionalListView.as_view(),
        name='admin-professional-list'
        ),
    path(
        'api/admin/clients/',
        ClientListView.as_view(),
        name='admin-client-list'
    ),
]
'''
