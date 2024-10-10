from django.shortcuts import render, get_object_or_404
from textblob import TextBlob
from langdetect import detect, LangDetectException
from googletrans import Translator, LANGUAGES
import nltk
from .models import AITopic
from .forms import TextInputForm

def index(request):
    topics = AITopic.objects.all()
    return render(request, 'learning/index.html', {'topics': topics})

def topic_detail(request, slug):
    topic = get_object_or_404(AITopic, slug=slug)
    return render(request, 'learning/topic_detail.html', {'topic': topic})

def analyze_text(request):
    form = TextInputForm()
    tokenized_text = None
    sentiment = None
    user_text = None
    pos = None
    detected_language = None
    translated_text = None

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['user_text']
            action = request.POST.get('action')

            if action == 'tokenize':
                tokenized_text = nltk.word_tokenize(user_text)
            elif action == 'sentiment':
                blob = TextBlob(user_text)
                sentiment = blob.sentiment
            elif action == 'pos':
                blob = TextBlob(user_text)
                pos = blob.tags
            elif action == 'translate':
                try:
                    detected_language = detect(user_text)
                    translator = Translator()
                    if detected_language == 'en':
                        translated_text = translator.translate(user_text,dest="tr")
                    if detected_language == 'tr':
                        translated_text = translator.translate(user_text,dest="en")
                except LangDetectException:
                    detected_language = "Language detection error. Please provide more text for detection."
                except Exception as e:
                    detected_language = f"Translation Error: {e}"

    return render(request, 'learning/analyze_text.html', {
        'form': form,
        'user_text': user_text,
        'tokenized_text': tokenized_text,
        'sentiment': sentiment,
        'pos': pos,
        'detected_language': detected_language,
        'translated_text': translated_text,
    })
