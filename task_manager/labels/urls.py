from django.urls import path
from task_manager.labels import views

app_name = 'labels'
urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels_list'),
    path('create/', views.CreateLabelsView.as_view(), name='create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='delete'),
]