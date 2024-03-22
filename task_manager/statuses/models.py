from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext


class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='statuses', null=True,
                               blank=True, verbose_name="Author")

    class Meta:
        verbose_name = gettext('Status')
        verbose_name_plural = gettext('Statuses')

    def __str__(self):
        return self.name
