from .models import Student
from .serializers import StudentSerializer
from .permissions import StudentModelPermission
from rest_framework.viewsets import ModelViewSet


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [StudentModelPermission]