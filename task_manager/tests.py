from django.test import TestCase
from django.urls import reverse


class GetIndexPageTestCase(TestCase):
    def setUp(self):
        'Инициализация перед выполнением теста'

    def test_mainpage(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_manager/index.html')

    def tearDown(self):
        'Действия после выполнения теста'
