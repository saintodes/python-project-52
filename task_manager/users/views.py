from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext as _

from task_manager.mixins import AuthPassesTestMixin
from task_manager.users.forms import RegisterUserForm


# Create your views here.
class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    extra_context = {'title': _("Registration")}
    success_url = reverse_lazy('login')
    success_message = _('The user has been successfully registered')


class UsersView(ListView):
    template_name = 'users/users_list.html'
    context_object_name = 'users_list'
    title_page = 'Users'

    def get_queryset(self):
        return get_user_model().objects.only('id', 'username', 'first_name', 'last_name', 'date_joined')


class UpdateUser(SuccessMessageMixin, AuthPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = RegisterUserForm
    template_name = 'users/update.html'
    extra_context = {'title': _('User update')}
    success_message = _('The user has been successfully modified')
    success_url = reverse_lazy('users:users_list')
    error_message = _('You do not have permission to change another user.')


class DeleteUser(SuccessMessageMixin, AuthPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    extra_context = {'title': _('Delete user')}
    success_message = _('The user has been successfully deleted')
    success_url = reverse_lazy('users:users_list')
    error_message = _('You do not have permission to change another user.')
