from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

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


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = 'users/update.html'
    extra_context = {'title': 'User update'}
    success_url = reverse_lazy('users:users_list')
    # permission_required = 'users.change_user'


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    extra_context = {'title': 'Delete user'}
    success_url = reverse_lazy('users:users_list')
