from django.urls import path
from enroll import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name='home-page'),
]
