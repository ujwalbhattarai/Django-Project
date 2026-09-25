from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from .forms import StudentForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required("students.view_student")
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

@login_required
@permission_required("students.view_student")
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

@login_required
@permission_required("students.add_student")
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

@login_required
@permission_required("students.change_student")
def student_update(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Student updated successfully!"
            )

            return redirect("students:student-list")

    else:
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

@login_required
@permission_required("students.delete_student")
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