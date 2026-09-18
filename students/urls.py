from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="student-list"),

    path(
        "<int:student_id>/",
        views.student_detail,
        name="student-detail"
    ),

    path(
        "create/",
        views.student_create,
        name="student-create"
    ),

    path(
        "<int:student_id>/edit/",
        views.student_update,
        name="student-update"
    ),

    path(
        "<int:student_id>/delete/",
        views.student_delete,
        name="student-delete"
    ),
]