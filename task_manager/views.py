from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.utils.translation import gettext as _

from task_manager.forms import LoginUserForm


# Create your views here.

def tasks_home(request):
    title = _("Main Page")
    context = {'title': title}
    return render(request, 'task_manager/index.html', context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'task_manager/login.html'
    extra_context = {'title': 'Авторизация'}

