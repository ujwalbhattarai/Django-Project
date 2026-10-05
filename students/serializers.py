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
            "profile_image",
            "document",
            "enrollments",
            "total_enrollments",
        ]
        read_only_fields = [
            "id",
            "enrollments",
            "total_enrollments",
        ]

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Age cannot be negative."
            )
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Name cannot be empty."
            )
        return value.strip()

    def get_total_enrollments(self, obj):
        return obj.enrollments.count()

    def validate_profile_image(self, value):
        allowed_types = [
            "image/jpeg",
            "image/png",
            "image/webp",
        ]

        if value.content_type not in allowed_types:
            raise serializers.ValidationError(
                "Only JPG, PNG, and WebP images are allowed."
            )

        max_size = 2 * 1024 * 1024  # 2 MB

        if value.size > max_size:
            raise serializers.ValidationError(
                "Image size cannot exceed 2 MB."
            )

        return value


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