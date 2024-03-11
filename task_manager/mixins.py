from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy



class AuthPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        user_being_edited = self.get_object()
        return self.request.user == user_being_edited or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, self.error_message)
        return redirect(reverse_lazy('users:users_list'))


class UserIsTaskCreatorOrSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        user = self.request.user
        return task.created_by_user_id == user or user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return redirect(reverse_lazy('tasks:tasks_list'))
