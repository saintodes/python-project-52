from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.mixins import UserIsTaskCreatorOrSuperUserMixin
from tasks.models import Tasks
from statuses.models import Status
from tasks.forms import CreateTaskForm
from task_manager.utils import FLASH_MESSAGES_TEXT


# Create your views here.
class TasksView(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    title_page = gettext('Tasks')

    def get_queryset(self):
        return Tasks.objects.only('id', 'name', 'status', 'created_by_user_id', 'time_create')


class TasksCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    template_name = 'tasks/create.html'
    extra_context = {'title': gettext("Create a task")}
    success_url = reverse_lazy('tasks:tasks_list')

    def form_valid(self, form):
        form.instance.created_by_user_id = self.request.user
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'tasks/update.html'
    extra_context = {'title': gettext('Task update')}
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = FLASH_MESSAGES_TEXT["change_task_data_auth_failed"]

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, FLASH_MESSAGES_TEXT["task_update_success"])
        return response


class TasksDeleteView(UserIsTaskCreatorOrSuperUserMixin, LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    extra_context = {'title': gettext('Delete a task')}
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = FLASH_MESSAGES_TEXT["change_task_data_auth_failed"]
    redirect_url = 'tasks:tasks_list'
    message_level = messages.ERROR

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, FLASH_MESSAGES_TEXT["status_delete_success"])
        return response
