from rest_framework import serializers
from .models import Student, Course, Enrollment
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    course_details = CourseSerializer(
        source="course",
        read_only=True
    )

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "course",
            "course_details",
            "enrollment_date",
            "status",
        ]
        read_only_fields = ["id", "enrollment_date"]



class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(
        many=True,
        read_only=True
    )
    total_enrollments = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "age",
            "enrollments",
            "total_enrollments",
        ]

    def get_total_enrollments(self, obj):
        return obj.enrollments.count()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)