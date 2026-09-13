from django.contrib import admin
from .models import Experience

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'category', 'is_ongoing', 'started_at')
    list_filter = ('category', 'ended_at')
    search_fields = ('role', 'organization', 'description')
