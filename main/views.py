import json
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from main.models import Experience, Education, Project
from main.forms import ProjectForm, ExperienceForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Profile views
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

# Experience views
def show_experience(request):
    role_query = request.GET.get("role", "").strip()
    experiences = Experience.objects.all().order_by('-created_at')

    # Filter berdasarkan role atau organisasi
    if role_query:
        experiences = experiences.filter(
            Q(role__icontains=role_query) | Q(organization__icontains=role_query)
        )
    
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "experiences": experiences,
        "role_query": role_query
    }
    
    return render(request, "experience.html", context)

# bagian menambah experience dengan form
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
    }
    return render(request, "experience_form.html", context)

# bagian mengupdate experience dengan form
def update_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
        "experience": experience,
        "update": True,
    }
    return render(request, "experience_form.html", context)

# bagian menghapus experience
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")

# Mengambil data dalam format JSON
def get_experience_json(request):
    role_query = request.GET.get("role", "").strip()
    experiences = Experience.objects.all()

    if role_query:
        experiences = experiences.filter(
            Q(role__icontains=role_query) | Q(organization__icontains=role_query)
        )

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def get_experience_json_by_id(request, id):
    experience = Experience.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", experience), content_type="application/json")

# Education views
def show_education(request):
    educations = Education.objects.all()
    
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "educations": educations,
    }
    return render(request, "education.html", context)

# Project views
def show_projects(request):
    projects = Project.objects.all()
    title_query = request.GET.get("title", "").strip()

    # Filter berdasarkan nama project
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

# bagian memambah project baru dengan form
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
    }
    return render(request, "projects_form.html", context)

# bagian mengupdate project dengan form
def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
        "project": project,
        "update": True,
    }

    return render(request, "projects_form.html", context)

# bagian menghapus project
def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")

    return redirect("main:show_projects")

# Mengambil data dalam format JSON 
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def get_projects_json_by_id(request, id):
    project = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", project), content_type="application/json")

