from django.contrib import admin
from .models import AITopic, Quiz

@admin.register(AITopic)
class AITopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('topic', 'question')
    search_fields = ('question', 'topic__title')
    list_filter = ('topic',)
