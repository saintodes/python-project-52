from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.statuses.forms import CreateStatusForm
from task_manager.statuses.models import Status


# Create your views here.
class StatusesView(LoginRequiredMixin, ListView):
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses_list'
    title_page = _('Statuses')

    def get_queryset(self):
        return Status.objects.only('id', 'name', 'time_create')


class CreateStatusView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = CreateStatusForm
    template_name = 'statuses/create.html'
    extra_context = {'title': _("Create status")}
    success_url = reverse_lazy('statuses:statuses_list')
    success_message = _('The status has been successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = CreateStatusForm
    template_name = 'statuses/update.html'
    extra_context = {'title': _('Status update')}
    success_url = reverse_lazy('statuses:statuses_list')
    success_message = _('The status has been successfully updated')


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    extra_context = {'title': _('Delete status')}
    success_url = reverse_lazy('statuses:statuses_list')
    success_message = _('The status has been successfully deleted')

    def post(self, request, *args, **kwargs):
        try:
            return super(StatusDeleteView, self).post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("It's impossible to delete the status because it's being used.")
            )
            return redirect('statuses:statuses_list')
