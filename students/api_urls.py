from django.urls import path
from .api_views import StudentListAPIView


urlpatterns = [
    path(
        "students/",
        StudentListAPIView.as_view(),
        name="student-api-list",
    ),
]