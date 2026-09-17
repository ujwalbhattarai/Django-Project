from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Student


def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

def student_detail(request, student_id):

    url = reverse("students:student-detail", args=[student_id])

    return JsonResponse({
        "id": student_id,
        "url": url,
        "Abhinay" : "Test"
    })