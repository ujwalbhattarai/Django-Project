from .models import Student
from .serializers import StudentSerializer
from .permissions import StudentModelPermission
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class StudentListCreateAPIView(ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]