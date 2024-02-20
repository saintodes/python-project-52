from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.

def tasks_home(request):
    title = _("Main Page")
    context = {'title': title}
    return render(request, 'task_manager/index.html', context)

