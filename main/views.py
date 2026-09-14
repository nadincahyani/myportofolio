from django.shortcuts import render

# Create your views here.
from main.models import Experience
from main.models import Education

def show_main(request):
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name" : "Nadin",
        "npm": "2506623332",
        "bio": (
            "Information Systems student at Universitas Indonesia, spending most days juggling coursework, teaching assistant duties, and student initiatives. "
            "Slowly becoming a familiar face around Fasilkom, for better or worse."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    experiences = Experience.objects.all()
    
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "experiences": experiences,
    }
    return render(request, "experience.html", context)

def show_education(request):
    educations = Education.objects.all()
    
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "experiences": educations,
    }
    return render(request, "education.html", context)
