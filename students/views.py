from django.http import HttpResponse, JsonResponse
from django.urls import reverse


def student_list(request):

    name = request.GET.get("name")

    if name:
        return JsonResponse({
            "message": "You searched for a student",
            "name": name
        })

    return JsonResponse({
        "message": "Student list"
    })

def student_detail(request, student_id):
    url = reverse("students:student-detail", args=[student_id])

    return JsonResponse({
        "id": student_id,
        "url": url
    })