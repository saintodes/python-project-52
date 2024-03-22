from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView

from task_manager.mixins import UserIsTaskCreatorOrSuperUserMixin
from task_manager.tasks.filters import TasksFilter
from task_manager.tasks.models import Tasks
from task_manager.tasks.forms import CreateTaskForm


class TasksView(LoginRequiredMixin, FilterView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    title_page = _('Tasks')
    filterset_class = TasksFilter


class TasksCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    template_name = 'tasks/create.html'
    extra_context = {'title': _("Create a task")}
    success_url = reverse_lazy('tasks:tasks_list')
    success_message = _('The task has been successfully created')

    def form_valid(self, form):
        form.instance.author_id = self.request.user
        return super().form_valid(form)


class TasksUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'tasks/update.html'
    extra_context = {'title': _('Task update')}
    success_message = _('The task has been successfully updated')
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = _('Only the author can delete the task')


class TasksDeleteView(UserIsTaskCreatorOrSuperUserMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    extra_context = {'title': _('Delete a task')}
    success_message = _('The task has been successfully deleted')
    success_url = reverse_lazy('tasks:tasks_list')
    error_message = _('Only the author can delete the task')
    redirect_url = 'tasks:tasks_list'
    message_level = messages.ERROR


class TaskShowView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task.html'
    model = Tasks
    context_object_name = 'task'
