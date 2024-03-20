from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ImageUpload

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'enroll/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        img = ImageUpload.objects.all()                 # all data access in database
        context = {'image': img}
        return context
    
