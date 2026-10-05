from students.models import Enrollment


def enroll_student(student, course):
    enrollment = Enrollment.objects.create(
        student=student,
        course=course
    )

    return enrollment