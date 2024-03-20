from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpUserCreationForm
from django.contrib import messages

# Create Signup views here.
class SignUpTemplateView(TemplateView):
    template_name = 'authentication/signup.html'
    
    def get_context_data(self, **kwargs):    # create get function
        context = super().get_context_data(**kwargs)
        fm = SignUpUserCreationForm()
        context = {'form':fm}
        return context
    
    
    def post(self, request):     # create post function
        fm = SignUpUserCreationForm(request.POST)
        
        if fm.is_valid():       # check valid form
            fm.save()
            
            # messages framework
            messages.success(request, 'Congratulations!!! your account has been created successfully')
            fm = SignUpUserCreationForm()       # empty form
        return render(request, 'authentication/signup.html', {'form':fm})





