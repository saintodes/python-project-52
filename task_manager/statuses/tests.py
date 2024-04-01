from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import CreateStatusForm
from .models import Status


class StatusModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='12345')
        cls.status = Status.objects.create(name='In Progress', author=cls.user)

    def test_status_content(self):
        self.assertEqual(self.status.name, 'In Progress')
        self.assertEqual(self.status.author, self.user)


class CreateStatusFormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'Completed'}
        form = CreateStatusForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'name': ''}
        form = CreateStatusForm(data=form_data)
        self.assertFalse(form.is_valid())


class StatusListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create multiple statuses to test the list view
        number_of_statuses = 5
        cls.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}', author=cls.user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('statuses:statuses_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_list.html')


class CreateStatusViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='12345')

    def test_create_status(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('statuses:create'), {'name': 'Testing'})
        self.assertRedirects(response, reverse('statuses:statuses_list'))


class StatusUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='12345')
        cls.status = Status.objects.create(name='In Progress', author=cls.user)

    def test_update_status(self):
        status_id = self.status.id
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('statuses:update', args=[status_id]), {'name': 'Updated Status'})
        self.assertRedirects(response, reverse('statuses:statuses_list'))


class StatusDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='12345')
        cls.status = Status.objects.create(name='In Progress', author=cls.user)

    def test_delete_status(self):
        status_id = self.status.id
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('statuses:delete', args=[status_id]))
        self.assertRedirects(response, reverse('statuses:statuses_list'))
