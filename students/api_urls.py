from django.urls import path
from .api_views import StudentListAPIView, StudentDetailAPIView


urlpatterns = [
    path(
        "students/",
        StudentListAPIView.as_view(),
        name="student-api-list",
    ),

    path(
        "students/<int:pk>/",
        StudentDetailAPIView.as_view(),
        name="student-api-detail",
    ),
]