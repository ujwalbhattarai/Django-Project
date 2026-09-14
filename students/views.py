from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


def student_list(request):

    students = [
        {"id": 1, "name": "Ram", "age": 20},
        {"id": 2, "name": "Sita", "age": 21},
        {"id": 3, "name": "Hari", "age": 19},
    ]

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def student_detail(request, student_id):

    url = reverse("students:student-detail", args=[student_id])

    return JsonResponse({
        "id": student_id,
        "url": url
    })