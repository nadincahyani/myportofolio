import uuid
from django.db import models

# Create your models here.
class Experience(models.Model):
    class Meta: 
        ordering = ['-started_at']
        
    EXPERIENCE_CHOICES = [
        ('organization', 'Organization'),
        ('committee', 'Committee'),
        ('teaching-assistant', 'Teaching Assistant'),
        ('volunteer', 'Volunteer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=150, default='-')
    organization = models.CharField(max_length=200, default='-')
    description = models.TextField()
    category = models.CharField(max_length=30, choices=EXPERIENCE_CHOICES, default='organization')

    date_display = models.CharField(max_length=100, blank=True, null=True, help_text="Contoh: May 2026 - Present")
    documentation_url = models.URLField(blank=True, null=True, help_text="Paste link foto di sini")

    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} - {self.organization}"
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.CharField(max_length=50, blank=True, null=True) # contoh: "2025" atau "Present"
    is_ongoing = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return self.institution