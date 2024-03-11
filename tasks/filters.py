import django_filters
from django.contrib.auth import get_user_model
from django.forms import CheckboxInput, Select
from django.utils.translation import gettext

from labels.models import Labels
from statuses.models import Status
from tasks.models import Tasks


class TasksFilter(django_filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels', 'my_tasks']

    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all(), widget=Select(attrs={'class': 'form-select'}))
    executor = django_filters.ModelChoiceFilter(queryset=get_user_model().objects.all(), label=gettext('Executor'), widget=Select(attrs={'class': 'form-select'}))
    labels = django_filters.ModelChoiceFilter(queryset=Labels.objects.all(), label=gettext('Label'), widget=Select(attrs={'class': 'form-select'}))
    my_tasks = django_filters.BooleanFilter(label=gettext('My tasks only'), widget=CheckboxInput(), method='get_my_tasks')

    def get_my_tasks(self, queryset, name, value):
        result = queryset.filter(created_by_user_id=self.request.user.id)
        return result if value else queryset
