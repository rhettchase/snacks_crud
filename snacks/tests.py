from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        # Create a User instance to use as the purchaser
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Now use the created User instance for the purchaser field
        self.snack = Snack.objects.create(title="chips", purchaser=self.user, description="Test Description")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "chips")
        
    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "chips")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args=[1]))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: testuser")
        self.assertTemplateUsed(response, "snack_detail.html")
        
    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Cheetos",
                "purchaser": self.user.id,
                "description": "crunchy cheese puffs",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Cheetos")
        
    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args=[1]),
            {"title": "Updated title", "purchaser": self.user.id, "description": "updated description"},
        )

        self.assertRedirects(
            response, reverse("snack_detail", args=[1]), target_status_code=200
        )
        
    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args=[25]),
            {"title": "Updated title", "purchaser": self.user.id, "description": "updated description"},
        )

        self.assertEqual(response.status_code, 404)
        
    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args=[1]))
        self.assertEqual(response.status_code, 200)
        
    def test_model(self):
        snack = Snack.objects.create(title="cheez-its", purchaser=self.user, description="cheesy")
        self.assertEqual(snack.title, "cheez-its")
        self.assertEqual(snack.purchaser, self.user)
        self.assertEqual(snack.description, "cheesy")