from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from ..models import Professional, Service, Profession
from ..serializers import ServiceSerializer, ProfessionSerializer, ProfessionalSerializer

class SearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SearchView(APIView):
    permission_classes = [permissions.AllowAny]
    
    pagination_class = SearchPagination

    def get(self, request):
        query = request.query_params.get('q', '').strip().lower()
        search_type = request.query_params.get('type', 'all')

        if not query:
            return Response({"error": "Veuillez fournir un terme de recherche."}, status=400)

        results = {}

        if search_type in ['all', 'services']:
            services = Service.objects.filter(
                Q(service_name__icontains=query) |
                Q(service_category__icontains=query)
            )
            results['services'] = ServiceSerializer(services, many=True).data

        if search_type in ['all', 'professions']:
            professions = Profession.objects.filter(name__icontains=query)
            results['professions'] = ProfessionSerializer(professions, many=True).data

        if search_type in ['all', 'professionals']:
            professionals = Professional.objects.filter(
                Q(services__service_name__icontains=query) |
                Q(services__service_category__icontains=query) |
                Q(profession__name__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            ).distinct().select_related('profession').prefetch_related('services')

            paginator = self.pagination_class()
            paginated_professionals = paginator.paginate_queryset(professionals, request)
            serialized_professionals = ProfessionalSerializer(paginated_professionals, many=True).data

            results['professionals'] = {
                'results': serialized_professionals,
                'count': professionals.count(),
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }

        return Response(results)
