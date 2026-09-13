from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience


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

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.role)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        expected_str = f"{self.experience.role} - {self.experience.organization}"
        self.assertEqual(str(self.experience), expected_str)
        self.assertEqual(self.experience.category, "teaching-assistant")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.role)
        self.assertContains(response, self.experience.organization)
        self.assertContains(response, self.experience.description)

        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")
