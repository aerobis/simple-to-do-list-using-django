from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='todo/logout.html', name="logout")),
    path('register/',auth_views.RegisterView.as_view(template_name='todo/register.html'), name="register"),
]