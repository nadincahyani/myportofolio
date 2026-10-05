import json
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.html import escape

from main.models import Experience, Education, Project
from django.contrib.auth.models import User

class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="adminpassword123",
            email="admin@example.com"
        )

        self.experience = Experience.objects.create(
            role="Teaching Assistant for Discrete Mathemathics 1",
            organization="Fakultas Ilmu Komputer, Universitas Indonesia",
            description="Supporting a class of 55 students as a Teaching Assistant for Discrete Mathematics 1. " \
            "Responsible for supervising quizzes and examinations, grading and evaluating quiz submissions, and " \
            "conducting review and assistance sessions to help students prepare for examinations, while supporting students throughout the learning process.",
            category="teaching-assistant",
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="Bachelor of Information Systems",
            start_year=2024,
            end_year=2028,
            is_ongoing=True,
        )

        self.project = Project.objects.create(
            title="Living Green Lantern's Bird",
            tech_stack="Green Lantern's Ring, Creativity, Arts, Nature",
            description= "In my training program with Hal Jordan, he told me to create some living thing with his green lantern's ring in order to evaluate my creativity skill. I've created Green Living Bird who can live miles without the ring power and survived up to 12+ hours.",
            project_url="",
            project_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMQQ0x2GeB4AH8xPAmf77qV_btUQyVb24Y56R4z2g3YA&s=10"
        )
     
    # Test Main
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    # Test Experience
    def test_experience_model(self):
        expected_str = f"{self.experience.role} - {self.experience.organization}"
        self.assertEqual(str(self.experience), expected_str)
        self.assertEqual(self.experience.category, "teaching-assistant")

    def test_experience_page(self):
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)

        api_response = self.client.get('/api/experience/')
        self.assertEqual(api_response.status_code, 200)
        self.assertContains(api_response, self.experience.role)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")

    def test_experience_search_filter(self):
        api_response = self.client.get('/api/experience/?role=Teaching%20Assistant')
        self.assertEqual(api_response.status_code, 200)
        self.assertContains(api_response, self.experience.role)

    def test_get_experience_json_api(self):
        """Uji endpoint GET JSON untuk mengambil daftar experience via AJAX"""
        response = self.client.get(reverse("main:get_experience_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    # Test Education
    def test_education_page_displays_data(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.institution)
        self.assertContains(response, self.education.degree)

    def test_education_page_ongoing_status(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Present")
        self.assertContains(response, 'class="edu-status-dot"')

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No education details has been added yet.")

    # Test Project
    def test_project_page_displays_data(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, 'id="project-search-form"')

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditambahkan atau ditemukan.")
    
    def test_create_project_ajax_unauthorized(self):
        """Uji perlindungan hak akses: guest/non-admin tidak boleh buat project (Status 403)"""
        payload = {
            "title": "Unauthorized Project",
            "tech_stack": "Python",
            "description": "Test description",
        }
            
        response = self.client.post(reverse("main:create_project_ajax"), data=payload)
        self.assertIn(response.status_code, [403, 302])
    
    def test_create_project_ajax_invalid_data(self):
        """Uji kirim data form tidak valid (Status 400 Bad Request)"""
        self.client.login(username="admin", password="adminpassword123")
    
        response = self.client.post(reverse("main:create_project_ajax"), data={})
        self.assertEqual(response.status_code, 400)

    def test_project_api_returns_data(self):
        response = self.client.get('/api/projects/')  # Sesuaikan URL API Anda
        self.assertEqual(response.status_code, 200)
    
        json_data = response.json()
        titles = [item['fields']['title'] for item in json_data]
        self.assertIn(self.project.title, titles)
