from django.contrib import admin
from task_manager.tasks.models import Tasks


# Register your models here.
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'executor', 'status', 'label', 'description',
              'time_create', 'time_update']
    readonly_fields = ['time_create', 'time_update']
    list_display = ['name', 'author', 'executor', 'status', 'description',
                    'time_create', 'time_update']
    list_display_links = ['name', 'executor']
