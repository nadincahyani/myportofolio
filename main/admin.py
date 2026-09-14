from django.contrib import admin
from .models import Experience

# Register your models here.
from main.models import Experience
admin.site.register(Experience)
