# Generated by Django 5.0.2 on 2024-03-06 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_status_delete_statuses'),
        ('tasks', '0003_tasks_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='statuses.status', verbose_name='Status'),
        ),
    ]
