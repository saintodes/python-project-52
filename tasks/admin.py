from django.contrib import admin
from tasks.models import Task
# Register your models here.
@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    fields = ['name', 'created_by_user_id', 'performer_user_id', 'time_create', 'time_update']
    readonly_fields = ['time_create', 'time_update']
    list_display = ['name', 'created_by_user_id', 'performer_user_id', 'time_create', 'time_update']
    list_display_links = ['name', 'performer_user_id']
