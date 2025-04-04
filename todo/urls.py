from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #FOR THE LOGIN, LOGOUT AND REGISTER
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='todo/logout.html'), name="logout"),
    path('register/', views.register, name="register"),

    #FOR THE CRUD VIEWS
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete')    
]