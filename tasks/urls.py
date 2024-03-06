from django.urls import path
from tasks import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks_list'),
    path('create/', views.TasksCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.TasksUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TasksDeleteView.as_view(), name='delete'),
]