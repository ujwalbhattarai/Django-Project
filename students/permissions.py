from rest_framework.permissions import BasePermission


class StudentModelPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method == "GET":
            return request.user.has_perm(
                "students.view_student"
            )

        if request.method == "POST":
            return request.user.has_perm(
                "students.add_student"
            )

        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm(
                "students.change_student"
            )

        if request.method == "DELETE":
            return request.user.has_perm(
                "students.delete_student"
            )

        return False