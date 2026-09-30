from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from .permissions import StudentModelPermission
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView


class StudentListAPIView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]

    
class StudentCreateAPIView(CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [StudentModelPermission]


class StudentDetailAPIView(APIView):

    permission_classes = [StudentModelPermission]

    def get(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        serializer = StudentSerializer(student)

        return Response(serializer.data)

    def put(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        student.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )