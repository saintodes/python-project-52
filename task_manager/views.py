from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from task_manager.forms import LoginUserForm


def tasks_home(request):
    title = _("Main Page")
    context = {'title': _(title)}
    return render(request, 'task_manager/index.html', context)


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'task_manager/login.html'
    extra_context = {'title': _('Authorisation')}
    success_message = _('You are logged in')
    next_page = '/'


class LogoutUser(LogoutView):

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
