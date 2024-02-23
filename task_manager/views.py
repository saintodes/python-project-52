from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from task_manager.utils import FLASH_MESSAGES_TEXT

from task_manager.forms import LoginUserForm


def tasks_home(request):
    title = gettext("Main Page")
    context = {'title': gettext(title)}
    return render(request, 'task_manager/index.html', context)


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'task_manager/login.html'
    extra_context = {'title': gettext('Authorisation')}
    success_message = FLASH_MESSAGES_TEXT['login_success']


class LogoutUser(LogoutView):
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, FLASH_MESSAGES_TEXT['logout_success'])
        return super().dispatch(request, *args, **kwargs)
