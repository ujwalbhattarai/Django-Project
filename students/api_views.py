from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from .permissions import StudentModelPermission
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView


class StudentListAPIView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]

    
class StudentCreateAPIView(CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]


class StudentRetrieveAPIView(RetrieveAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]


class StudentUpdateAPIView(UpdateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]

    def delete(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        student.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )