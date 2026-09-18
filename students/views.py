from django.http import JsonResponse
from django.shortcuts import render
from .models import Student


from django.http import JsonResponse
from django.shortcuts import render

from .models import Student


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )


def student_create(request):
    return render(
        request,
        "students/student_form.html"
    )


def student_update(request, student_id):
    student = Student.objects.get(id=student_id)

    return render(
        request,
        "students/student_form.html",
        {"student": student}
    )


def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)

    return JsonResponse({
        "message": f"Delete student {student.name}"
    })