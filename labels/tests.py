from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import CreateLabelsForm
from .models import Labels


class LabelsModelTest(TestCase):
    def test_labels_creation(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass123')
        label = Labels.objects.create(name='Test Label', author=user)
        self.assertEqual(label.name, 'Test Label')
        self.assertEqual(label.author, user)


class CreateLabelsFormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'Valid Label Name'}
        form = CreateLabelsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_due_to_long_name(self):
        form_data = {'name': 'x' * 151}  # Exceeds the 150 character limit
        form = CreateLabelsForm(data=form_data)
        self.assertFalse(form.is_valid())


class CreateLabelsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/labels/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/create.html')

    def test_form_submission(self):
        response = self.client.post(reverse('labels:create'), {'name': 'Test Label'})
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('labels:create'))
        self.assertRedirects(response,
                             f"/login/?next={reverse('labels:create')}")

    def test_redirect_if_not_logged_in(self):
        self.client.logout()  # Ensure the user is logged out
        response = self.client.get(reverse('labels:create'))
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, f"/login/?next={reverse('labels:create')}")
