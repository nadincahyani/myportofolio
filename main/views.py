from django.shortcuts import render

# Create your views here.
from main.models import Experience


def show_main(request):
    context = {
        "name": "Nadin Putri Cahyani",
        "npm": "2506623332",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia, spending most days juggling coursework, teaching assistant duties, and student initiatives. "
            "Slowly becoming a familiar face around Fasilkom, for better or worse."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nadin Putri Cahyani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
