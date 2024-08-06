# pages/views.py

from django.views.generic import TemplateView

class ChatBotTemplateView(TemplateView):
    template_name = 'pages/chatbot.html'
