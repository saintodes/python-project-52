from django.urls import path
from task_manager.statuses import views

app_name = 'statuses'
urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses_list'),
    path('create/', views.CreateStatusView.as_view(), name='create'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='delete'),
]