from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def student_detail(request, student_id):
    student = get_object_or_404(
        Student,
        id=student_id
    )

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )


def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Student created successfully!"
            )

            return redirect("students:student-list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )


def student_update(request, student_id):

    student = get_object_or_404(
    Student,
    id=student_id
)

    form = StudentForm(
        instance=student
    )

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "student": student
        }
    )


def student_delete(request, student_id):

    student = get_object_or_404(
    Student,
    id=student_id
)

    if request.method == "POST":

        student.delete()

        messages.success(
            request,
            "Student deleted successfully!"
        )

        return redirect("students:student-list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )