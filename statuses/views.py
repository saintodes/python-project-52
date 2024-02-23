from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from statuses.forms import CreateStatusForm
from statuses.models import Status


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


class StatusDeleteUser(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    extra_context = {'title': gettext('Delete status')}
    success_url = reverse_lazy('statuses:statuses_list')
