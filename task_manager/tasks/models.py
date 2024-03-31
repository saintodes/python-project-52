from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tasks(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'), unique=True)
    description = models.CharField(max_length=150, verbose_name=_('Description'), null=True, blank=True)

    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT, null=True, verbose_name=_('Status'),
                               db_index=True)
    labels = models.ManyToManyField('labels.Labels', blank=True, verbose_name=_('Label'),
                                   related_name='task_labels')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Time'))
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='author',
                                  null=True, blank=True, verbose_name=_("Author"), db_index=True)
    executor = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='executor',
                                    null=True, blank=True, verbose_name=_("Executor"), db_index=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.name
