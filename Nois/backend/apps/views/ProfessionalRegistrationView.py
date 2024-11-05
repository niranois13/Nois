from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db import transaction
from . import ProfessionalViewSet, ProfessionViewSet, ProfessionalAddressViewSet
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfessionalRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def post(self, request):
        factory = APIRequestFactory()

        professional_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'phone_number': request.data.get('phone_number', ''),
            'is_mobile': request.data.get('is_mobile'),
            'intervention_radius': request.data.get('intervention_radius'),
            'profession': None,
        }

        professional_view = ProfessionalViewSet.as_view({'post': 'create'})
        professional_request = factory.post('api/professionals/', professional_data)
        professional_response = professional_view(professional_request)
        if professional_response.status_code != 201:
            return professional_response

        profession_data = {
            'name': request.data.get('name'),
            'custom_profession': request.data.get('custom_profession', ''),
            'proposed_by_slug': professional_response.data['slug'],
        }

        profession_view = ProfessionViewSet.as_view({'post': 'create'})
        profession_request = factory.post('api/professions/', profession_data)
        profession_response = profession_view(profession_request)
        if profession_response.status_code != 201:
            return profession_response

        professional_update_view = ProfessionalViewSet.as_view({'patch': 'partial_update'})
        professional_update_request = factory.patch(
            f'api/professionals/{professional_response.data["slug"]}/',
            {'profession': profession_response.data['id']}
        )
        professional_update_response = professional_update_view(
            professional_update_request,
            slug=professional_response.data['slug']
        )
        if professional_update_response.status_code != 200:
            return professional_update_response

        address_data = request.data.get('Address', '')
        address_data['professional'] = professional_response.data['slug']
        address_view = ProfessionalAddressViewSet.as_view({'post': 'create'})
        address_request = factory.post(f'api/professionals/{professional_response.data["slug"]}/address/', address_data)
        address_response = address_view(address_request, slug=professional_response.data['slug'])
        if address_response.status_code != 201:
            return address_response

        return Response(professional_response.data, status=status.HTTP_201_CREATED)
