from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.users.forms import RegisterUserForm


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
            'first_name': 'test first name',
            'last_name': 'test last name',
        }
        response = self.client.post(reverse('users:create'), user_data)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertRedirects(response, reverse('login'))

    def test_register_view_post_error(self):
        response = self.client.post(reverse('users:create'), {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(get_user_model().objects.count(), 0)


class RegisterUserFormTest(TestCase):

    def test_password_len_validation(self):
        form = RegisterUserForm(data={
            'username': 'testuser',
            'password1': '12',
            'password2': '12',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password1'],
            ['Ваш пароль должен содержать как минимум 3 символа.']
        )

    def test_username_validation(self):
        form = RegisterUserForm(data={
            'username': '<> wrong name',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            ['Введите правильное имя пользователя. Оно может содержать '
             'только буквы, цифры и знаки @/./+/-/_.']
        )

    def test_form_with_valid_data(self):
        form = RegisterUserForm(data={
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'first_name': 'testfname',
            'last_name': 'testlname'
        })
        self.assertTrue(form.is_valid())

    def test_username_max_len_validation(self):
        form = RegisterUserForm(
            data={
                'username': '1' * 151,
                'password1': 'password123',
                'password2': 'password123',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            ['Имя пользователя не может превышать 150 символов ']
        )


class UsersViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username='user1', password='password123')
        get_user_model().objects.create_user(username='user2', password='password123')

    def test_users_list_page(self):
        response = self.client.get(reverse('users:users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_list.html')
        self.assertEqual(len(response.context['users_list']), 2)


class UpdateUserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='updateuser',
            password='password123',
        )

    def test_update_user_page(self):
        self.client.login(username='updateuser', password='password123')
        response = self.client.get(reverse('users:update', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

    def test_successful_user_update(self):
        self.client.login(username='updateuser', password='password123')
        response = self.client.post(reverse('users:update', kwargs={'pk': self.user.pk}), {
            'username': 'updateduser',
            'first_name': 'new_first_name',
            'last_name': 'new_last_name',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        if response.status_code != 302:
            print("Form errors:", response.context['form'].errors)
        self.assertRedirects(response, reverse('users:users_list'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.first_name, 'new_first_name')
        self.assertEqual(self.user.last_name, 'new_last_name')

    def test_update_user_form_errors(self):
        self.client.login(username='updateuser', password='password123')
        response = self.client.post(reverse('users:update', kwargs={'pk': self.user.pk}), {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())


class DeleteUserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='deleteuser',
            password='password123'
        )

    def test_delete_user_page(self):
        self.client.login(username='deleteuser', password='password123')
        response = self.client.get(reverse('users:delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

    def test_successful_user_deletion(self):
        self.client.login(username='deleteuser', password='password123')
        response = self.client.post(reverse('users:delete', kwargs={'pk': self.user.pk}))
        self.assertRedirects(response, reverse('users:users_list'))
        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(pk=self.user.pk)
