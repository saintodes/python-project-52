from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView

from task_manager.mixins import UserIsTaskCreatorOrSuperUserMixin
from tasks.filters import TasksFilter
from tasks.models import Tasks
from tasks.forms import CreateTaskForm
from task_manager.utils import FLASH_MESSAGES_TEXT


class TasksView(LoginRequiredMixin, FilterView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    title_page = gettext('Tasks')
    filterset_class = TasksFilter


class TasksCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    template_name = 'tasks/create.html'
    extra_context = {'title': gettext("Create a task")}
    success_url = reverse_lazy('tasks:tasks_list')
    success_message = FLASH_MESSAGES_TEXT['task_create_success']

    def form_valid(self, form):
        form.instance.created_by_user_id = self.request.user
        return super().form_valid(form)


class TasksUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'tasks/update.html'
    extra_context = {'title': gettext('Task update')}
    success_message = FLASH_MESSAGES_TEXT['task_update_success']
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = FLASH_MESSAGES_TEXT["change_task_data_auth_failed"]


class TasksDeleteView(UserIsTaskCreatorOrSuperUserMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    extra_context = {'title': gettext('Delete a task')}
    success_message = FLASH_MESSAGES_TEXT['task_create_success']
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = FLASH_MESSAGES_TEXT["change_task_data_auth_failed"]
    redirect_url = 'tasks:tasks_list'
    message_level = messages.ERROR


class TaskShowView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task.html'
    model = Tasks
    context_object_name = 'task'
