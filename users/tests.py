from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from users.forms import RegisterUserForm


class RegisterUserTestCase(TestCase):

    def test_register_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_successful_registration(self):
        user_data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'test@test.com'
        }
        response = self.client.post(reverse('users:create'), user_data)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse('login'))

    def test_register_view_post_error(self):
        response = self.client.post(reverse('users:create'), {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(User.objects.count(), 0)


class RegisterUserFormTest(TestCase):

    def test_password_len_validation(self):
        form = RegisterUserForm(data={
            'username': 'testuser',
            'password1': '12',
            'password2': '12',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], ['Your password must contain at least 3 characters.'])

    def test_username_validation(self):
        form = RegisterUserForm(data={
            'username': '<> wrong name',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],
                         ['The username can only contain letters, numbers, and the symbols @/./+/-/_.'])

    def test_form_with_valid_data(self):
        form = RegisterUserForm(data={
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertTrue(form.is_valid())

    def test_username_max_len_validation(self):
        form = RegisterUserForm(data={
            'username': '1' * 151,
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['The username length cannot exceed 150 characters.'])


class UsersViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='user1', password='password123')
        User.objects.create_user(username='user2', password='password123')

    def test_users_list_page(self):
        response = self.client.get(reverse('users:users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_list.html')
        self.assertEqual(len(response.context['users_list']), 2)
