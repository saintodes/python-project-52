from django.contrib.auth import get_user_model
from django.forms import CheckboxInput, Select
from django.utils.translation import gettext
from django_filters import BooleanFilter, ModelChoiceFilter, FilterSet

from task_manager.labels.models import Labels
from task_manager.statuses.models import Status
from task_manager.tasks.models import Tasks


class TasksFilter(FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels', 'my_tasks']

    status = ModelChoiceFilter(queryset=Status.objects.all(), widget=Select(attrs={'class': 'form-select'}))
    executor = ModelChoiceFilter(queryset=get_user_model().objects.all(), label=gettext('Executor'), widget=Select(attrs={'class': 'form-select'}))
    labels = ModelChoiceFilter(queryset=Labels.objects.all(), label=gettext('Label'), widget=Select(attrs={'class': 'form-select'}))
    my_tasks = BooleanFilter(label=gettext('My tasks only'), widget=CheckboxInput(), method='get_my_tasks')

    def get_my_tasks(self, queryset, name, value):
        result = queryset.filter(author=self.request.user.id)
        return result if value else queryset
