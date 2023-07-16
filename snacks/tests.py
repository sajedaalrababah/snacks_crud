from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model


# Create your tests here.
class SnackTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snacks_list.html")
        self.assertTemplateUsed(response, "base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="teas@email.com", password="1234"
        )

        self.snack = Snack.objects.create(
            title="test", description="test info", purchaser=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), "test")

    def test_detail_view(self):
        url = reverse("snack_detail", args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_create_view(self):
        obj = {
            "title": "test2",
            "description": "info...",
            "purchaser": self.user.id,
        }

        url = reverse("create_snack")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("snack_detail", args=[2]))