from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from ..models import Professional
from ..serializers import ServiceSerializer, ProfessionSerializer, ProfessionalSerializer

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')

        # Recherche dans les services
        services = Service.objects.filter(
            service_name__icontains=query
        ) | Service.objects.filter(
            service_category__icontains=query
        )

        # Recherche dans les professions
        professions = Profession.objects.filter(name__icontains=query)

        # Récupérer les professionnels liés aux services et professions trouvés
        professionals = Professional.objects.filter(
            services__in=services
        ) | Professional.objects.filter(
            profession__in=professions
        ).distinct()

        # Sérialiser les résultats
        service_serializer = ServiceSerializer(services, many=True)
        profession_serializer = ProfessionSerializer(professions, many=True)
        professional_serializer = ProfessionalSerializer(professionals, many=True)

        return Response({
            'services': service_serializer.data,
            'professions': profession_serializer.data,
            'professionals': professional_serializer.data
        })
