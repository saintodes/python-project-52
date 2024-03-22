from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CreateLabelsForm
from .models import Labels


# Create your views here.
class LabelsView(LoginRequiredMixin, ListView):
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels_list'
    title_page = _('Labels')

    def get_queryset(self):
        return Labels.objects.only('id', 'name', 'time_create')


class CreateLabelsView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = CreateLabelsForm
    template_name = 'labels/create.html'
    extra_context = {'title': _("Create a label")}
    success_url = reverse_lazy('labels:labels_list')
    success_message = _('The label has been successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Labels
    form_class = CreateLabelsForm
    template_name = 'labels/update.html'
    extra_context = {'title': _('Label update')}
    success_url = reverse_lazy('labels:labels_list')
    success_message = _('The label has been successfully updated')


class LabelDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    extra_context = {'title': _('Delete a label')}
    success_url = reverse_lazy('labels:labels_list')
    success_message = _('The label has been successfully deleted')

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_labels.exists():
            messages.error(request, _("It's impossible to delete the label because it's being used."))
            return redirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)
