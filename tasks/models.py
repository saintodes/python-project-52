from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext


class Tasks(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)
    description = models.CharField(max_length=150, verbose_name='Description', null=True)

    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT, null=True, verbose_name='Status',
                               db_index=True)
    label = models.ManyToManyField('labels.Labels', blank=True, verbose_name=gettext('Label'),
                                   related_name='task_labels')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    created_by_user_id = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='author',
                                           null=True, blank=True, verbose_name="Author", db_index=True)
    performer_user_id = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='performer',
                                          null=True, blank=True, verbose_name="Performer", db_index=True)

    class Meta:
        verbose_name = gettext('Task')
        verbose_name_plural = gettext('Tasks')

    def __str__(self):
        return self.name
