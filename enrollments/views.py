
from rest_framework import viewsets
from .models import Enrollment
from .serializers import EnrollmentSerializer
from rest_framework.permissions import IsAuthenticated
class EnrollmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
