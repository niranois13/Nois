from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from ..permissions import IsOwnerOrAdmin
from ..models import Professional
from ..serializers import ProfessionalSerializer


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

'''
class ProfessionalRegistrationView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = ProfessionalRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            professional = serializer.save()
            return Response({
                'message': 'Professional enregistré avec succes',
                'professional_id': professional.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessionalListView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        professionals = Professional.objects.all()
        serializer = ProfessionalListSerializer(professionals, many=True)
        return Response(serializer.data)
'''
