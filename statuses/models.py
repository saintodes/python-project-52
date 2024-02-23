from django.contrib.auth import get_user_model
from django.db import models


class Status(models.Model):
    class IsPublished(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    name = models.CharField(max_length=150, verbose_name='Name', unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update Time')
    is_published = models.IntegerField(choices=IsPublished.choices, default=IsPublished.DRAFT,
                                       verbose_name="Publication Status")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='statuses', null=True,
                               blank=True, verbose_name="Author")

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name
