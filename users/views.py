from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterUserForm


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy('login')
