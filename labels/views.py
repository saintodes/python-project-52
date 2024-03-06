from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CreateLabelsForm
from .models import Labels
from task_manager.utils import FLASH_MESSAGES_TEXT


# Create your views here.
class LabelsView(LoginRequiredMixin, ListView):
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels_list'
    title_page = gettext('Labels')

    def get_queryset(self):
        return Labels.objects.only('id', 'name', 'time_create')


class CreateLabelsView(LoginRequiredMixin, CreateView):
    form_class = CreateLabelsForm
    template_name = 'labels/create.html'
    extra_context = {'title': gettext("Create a label")}
    success_url = reverse_lazy('labels:labels_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Labels
    form_class = CreateLabelsForm
    template_name = 'labels/update.html'
    extra_context = {'title': gettext('Label update')}
    success_url = reverse_lazy('labels:labels_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, FLASH_MESSAGES_TEXT["label_update_success"])
        return response


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    extra_context = {'title': gettext('Delete a label')}
    success_url = reverse_lazy('labels:labels_list')

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_labels.exists():
            messages.error(request, FLASH_MESSAGES_TEXT['used_label_delete_failed'])
            return redirect(self.success_url)
        else:
            messages.success(request, FLASH_MESSAGES_TEXT["label_delete_success"])
            return super().post(request, *args, **kwargs)
