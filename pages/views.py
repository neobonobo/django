# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class ChatBotTemplateView(TemplateView):
    template_name = 'pages/chatbot.html'
 
def tahini_view(request):
    return render(request, 'pages/tahini_page.html') 
