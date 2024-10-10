from django.db import models

class AITopic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(help_text="Detailed explanation of the AI concept")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    topic = models.ForeignKey(AITopic, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)
