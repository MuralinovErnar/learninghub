from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    login_view,
    teacher_dashboard_view,
    student_dashboard_view,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Добавь эту строку
    path('teacher/dashboard/', teacher_dashboard_view, name='teacher_dashboard'),
    path('student/dashboard/', student_dashboard_view, name='student_dashboard'),
]
