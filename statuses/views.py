from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from statuses.forms import CreateStatusForm
from statuses.models import Status
from task_manager.utils import FLASH_MESSAGES_TEXT


# Create your views here.
class StatusesView(LoginRequiredMixin, ListView):
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses_list'
    title_page = gettext('Statuses')

    def get_queryset(self):
        return Status.objects.only('id', 'name', 'time_create')


class CreateStatusView(LoginRequiredMixin, CreateView):
    form_class = CreateStatusForm
    template_name = 'statuses/create.html'
    extra_context = {'title': gettext("Create status")}
    success_url = reverse_lazy('statuses:statuses_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = CreateStatusForm
    template_name = 'statuses/update.html'
    extra_context = {'title': gettext('Status update')}
    success_url = reverse_lazy('statuses:statuses_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, FLASH_MESSAGES_TEXT["status_update_success"])
        return response


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    extra_context = {'title': gettext('Delete status')}
    success_url = reverse_lazy('statuses:statuses_list')

    def post(self, request, *args, **kwargs):
        try:
            response = super(StatusDeleteView, self).post(request, *args, **kwargs)
            messages.success(request, gettext("Status deleted successfully"))
            return response
        except ProtectedError:
            messages.error(request, FLASH_MESSAGES_TEXT['used_status_delete_failed'])
            return redirect('statuses:statuses_list')
