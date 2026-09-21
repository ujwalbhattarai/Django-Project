from django.http import JsonResponse
from django.shortcuts import render, redirect
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

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")

        Student.objects.create(
            name=name,
            age=age
        )

        return redirect("students:student-list")

    return render(
        request,
        "students/student_form.html"
    )


def student_update(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")

        student.save()

        return redirect("students:student-list")

    return render(
        request,
        "students/student_form.html",
        {"student": student}
    )


def student_delete(request, student_id):

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        student.delete()

        return redirect("students:student-list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )