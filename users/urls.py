from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('', views.UsersView.as_view(), name='users_list'),
    path('create/', views.RegisterUser.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
]
