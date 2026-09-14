from django.contrib import admin

# Register your models here.
from main.models import Experience
admin.site.register(Experience)

from main.models import Education
admin.site.register(Education)
