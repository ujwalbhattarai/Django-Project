from django.contrib import admin, messages

from .models import Student, Course, StudentProfile, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age"]
    search_fields = ["name"]
    list_filter = ["age"]
    ordering = ["name"]
    fields = [
        "name",
        "age",
    ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ["name"]

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "address",
        "phone",
    ]

    search_fields = [
        "student__name",
        "address",
        "phone",
    ]

    fieldsets = (
        (
            "Student Information",
            {
                "fields": (
                    "student",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "address",
                    "phone",
                )
            },
        ),
    )

def mark_as_inactive(modeladmin, request, queryset):
    updated_count = queryset.update(
        status="inactive"
    )

    messages.success(
        request,
        f"{updated_count} enrollment(s) marked as inactive."
    )

def mark_as_active(modeladmin, request, queryset):
    updated_count = queryset.update(
            status="active"
    )

    messages.success(
        request,
        f"{updated_count} enrollment(s) marked as active."
    )

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "course",
        "enrollment_date",
        "status",
    ]

    search_fields = [
        "student__name",
        "course__name",
    ]

    list_filter = [
        "status",
        "course",
        "enrollment_date",
    ]

    fields = [
        "student",
        "course",
        "status",
    ]

    actions = [
        mark_as_inactive,
        mark_as_active,
    ]
