from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    courses = models.ManyToManyField(
    Course,
    related_name="students"
    )

    def __str__(self):
        return self.name


class StudentProfile(models.Model):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} Profile"