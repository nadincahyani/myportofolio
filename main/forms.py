from django.forms import ModelForm, TextInput, Textarea, URLInput, CheckboxInput, Select

from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "role",
            "organization",
            "description",
            "category",
            "is_ongoing",
            "documentation_url",
        ]

        labels = {
            "role": "Peran/Jabatan",
            "organization": "Organisasi/Instansi",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "is_ongoing": "Masih Berlangsung (Ongoing)",
            "documentation_url": "URL Dokumentasi",
        }

        widgets = {
            "role": TextInput(
                attrs={
                    "placeholder": "Teaching Assistant / Staff",
                    "maxlength": 200,
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "BEM Fasilkom UI / Universitas Indonesia",
                    "maxlength": 200,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan tanggung jawab dan pencapaianmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "is_ongoing": CheckboxInput(),
            "documentation_url": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }