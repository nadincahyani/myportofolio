from django.shortcuts import render

# Create your views here.
from main.models import Experience
from main.models import Education
from main.forms import ProjectForm
from main.models import Project

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    experiences = Experience.objects.all().order_by('-id')

    context = {
            "name": "Nadin Putri Cahyani",
            "close_name": "Nadin",
            "experiences": experiences,
        }
    
    return render(request, 'experience.html', {'experiences': experiences})

def show_education(request):
    educations = Education.objects.all()
    
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "educations": educations,
    }
    return render(request, "education.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nadin",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Nadin",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")
