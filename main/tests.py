from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.html import escape

from main.models import Experience, Education, Project


class MainTest(TestCase):
    def setUp(self):
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
        self.assertNotContains(response, self.experience.role)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    # Test Experience
    def test_experience_model(self):
        expected_str = f"{self.experience.role} - {self.experience.organization}"
        self.assertEqual(str(self.experience), expected_str)
        self.assertEqual(self.experience.category, "teaching-assistant")

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.role)
        self.assertContains(response, self.experience.organization)
        self.assertContains(response, self.experience.description)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_experience_search_filter(self):
        response_match = self.client.get(reverse("main:show_experience"), {"role": "Teaching Assistant"})
        self.assertEqual(response_match.status_code, 200)
        self.assertContains(response_match, self.experience.role)

        response_no_match = self.client.get(reverse("main:show_experience"), {"role": "RandomRoleNotFound"})
        self.assertEqual(response_no_match.status_code, 200)
        self.assertContains(response_no_match, "Tidak ada pengalaman dengan kata kunci tersebut.")

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
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, escape(self.project.title))
        self.assertContains(response, escape(self.project.tech_stack))
        self.assertContains(response, escape(self.project.description))

    def test_project_search_filter(self):
        response_match = self.client.get(reverse("main:show_projects"), {"title": "Green Lantern"})
        self.assertEqual(response_match.status_code, 200)
        self.assertContains(response_match, escape(self.project.title))

        response_no_match = self.client.get(reverse("main:show_projects"), {"title": "SinestroCorps"})
        self.assertEqual(response_no_match.status_code, 200)
        self.assertContains(response_no_match, "Tidak ada proyek dengan nama tersebut.")

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditambahkan.")

