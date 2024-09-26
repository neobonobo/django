# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

class HomePageView(View):
    def get(self, request):
        # Redirect authenticated users to the dashboard
        if request.user.is_authenticated:
            return redirect('daytrack/dashboard')
        # Otherwise, render the login form
        form = AuthenticationForm()
        return render(request, 'pages/home.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('daytrack/dashboard')  # Redirect to the dashboard after successful login
        
        # If login is invalid, return the form with error messages
        return render(request, 'pages/home.html', {'form': form, 'error': 'Invalid credentials. Please try again.'})
class ChatBotTemplateView(TemplateView):
    template_name = 'pages/chatbot.html'
def tahini_view(request):
    return render(request, 'pages/tahini_page.html') 

def cv_view(request):
    return render(request, 'pages/cv.html')
