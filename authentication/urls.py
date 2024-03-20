from django.urls import path
from authentication import views

urlpatterns = [
    path("signup/", views.SignUpTemplateView.as_view(), name='signup-page'),
    path("login/", views.loginView, name='login-page'),
    path("dashboard/", views.dashboard, name='dashboard-page'),
    path("logout/", views.logoutView, name='logout-page'),
]
