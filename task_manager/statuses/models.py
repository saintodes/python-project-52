from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'), unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Time'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Update Time'))
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='statuses', null=True,
                               blank=True, verbose_name=_("Author"))

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.name
