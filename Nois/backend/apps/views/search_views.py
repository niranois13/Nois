from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, Func, F, TextField, CharField
from unidecode import unidecode
import re
from ..models import Professional, User, Service
from ..serializers import ServiceSerializer, ProfessionalSerializer

class Unaccent(Func):
    function = 'unaccent'
    template = '%(function)s(%(expressions)s)'
    output_field = CharField()

class SearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SearchView(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = SearchPagination

    def get(self, request):
        # Récupération et nettoyage de la requête
        query = request.query_params.get('q', '').strip()
        search_type = request.query_params.get('type', 'all')
        query = unidecode(query)
        query = re.sub(r'[^a-zA-Z0-9\s\-,.]', '', query)
        query_terms = query.split()

        if not query_terms:
            return Response({"error": "Veuillez fournir un terme de recherche."}, status=400)

        results = {}



        # Recherche des services
        # if search_type in ['all', 'services']:
        #     services = Service.objects.filter(
        #         Q(service_name__icontains=query) |
        #         Q(custom_service_name__icontains=query) |
        #         Q(service_category__icontains=query) |
        #         Q(custom_service_category__icontains=query)
        #     )

        #     paginator = self.pagination_class()
        #     paginated_services = paginator.paginate_queryset(services, request)
        #     serialized_services = ServiceSerializer(paginated_services, many=True).data

        #     results['services'] = {
        #         'results': serialized_services,
        #         'count': services.count(),
        #         'next': paginator.get_next_link(),
        #         'previous': paginator.get_previous_link()
        #     }

        # Recherche des professionnels
        if search_type in ['all', 'professionals']:
            for term in query_terms:
                professionals = Professional.objects.filter(
                    Q(first_name__unaccent__icontains=term) ^
                    Q(last_name__unaccent__icontains=term) ^
                    Q(profession__unaccent__icontains=term) ^
                    Q(custom_profession__unaccent__icontains=term)
                ).exclude(role='PROFESSIONALS').distinct()

            paginator = self.pagination_class()
            paginated_professionals = paginator.paginate_queryset(professionals, request)
            serializer = ProfessionalSerializer(paginated_professionals, many=True, context={'request': request})
            serialized_professionals = serializer.data

            results['professionals'] = {
                'results': serialized_professionals,
                'count': professionals.count(),
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }

            return Response(results)
