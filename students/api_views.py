
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentSerializer
from .permissions import StudentModelPermission


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [StudentModelPermission]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["age"]
    search_fields = ["name"]
    ordering_fields = ["name", "age"]
    ordering = ["id"]