from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [path('create/', views.RegisterUser.as_view(), name='create'),

               ]
