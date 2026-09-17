from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class StudentProfile(models.Model):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} Profile"


class Enrollment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    enrollment_date = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        default="active"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course"
            )
        ]

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"