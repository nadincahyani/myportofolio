import datetime
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from main.models import Experience, Education, Project
from main.forms import ProjectForm, ExperienceForm

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Profile views
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Nadin Putri Cahyani",
        "close_name" : "Nadin",
        "npm": "2506623332",
        "bio": (
            "Information Systems student at Universitas Indonesia, spending most days juggling coursework, teaching assistant duties, and student initiatives. "
            "Slowly becoming a familiar face around Fasilkom, for better or worse."
        ),
        "last_login": last_login,
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
@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
@login_required(login_url="/login/")
def delete_project(request, id):
    if not request.user.is_superuser:
            raise PermissionDenied
    
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

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

def get_projects_json_by_id(request, id):
    project = Project.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", project), content_type="application/json")

# Fungsi Register
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
    }

    return render(request, "register.html", context)

# View Login
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Nadin Putri Cahyani",
        "close_name": "Nadin",
        "form": form,
    }
    return render(request, "login.html", context)

# View Logout
def logout_user(request):
    logout(request)
    return redirect("main:show_main")

# Menambahkan Star
@login_required(login_url="/login/")
def toggle_star(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")
    
