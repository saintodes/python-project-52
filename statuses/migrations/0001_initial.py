# Generated by Django 5.0.2 on 2024-02-23 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Имя')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time create')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time update')),
                ('is_published', models.BooleanField(choices=[(False, 'Draft'), (True, 'Published')], default=0, verbose_name='Bind status')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
