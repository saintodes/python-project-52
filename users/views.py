from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Value
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from users.forms import RegisterUserForm


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy('login')


class UsersView(ListView):
    template_name = 'users/users_list.html'
    context_object_name = 'users_list'
    title_page = 'Users'

    def get_queryset(self):
        return User.objects.only('id', 'username', 'first_name', 'last_name', 'date_joined')
