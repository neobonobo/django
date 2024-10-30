import os
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from django.shortcuts import render, get_object_or_404
from textblob import TextBlob
from langdetect import detect, LangDetectException
import nltk
from .models import AITopic
from .forms import TextInputForm
import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
#model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv('OPENAI_API_KEY'))
user_memories = {}
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You talk a dominant, assertive and directive woman. Be aware that you are talking to adult man. Your name is Root",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
def interests(request):
    return render(request, 'learning/interests.html')
def ai_view(request):
    return render(request, 'learning/ai.html')

# Memory dictionary to store user-specific memories
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from typing import Sequence

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    chain = prompt | model
    response = chain.invoke(state)
    return {"messages": response}

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Langchain chatbot view
def chatbot_view(request):
    form = TextInputForm()
    response = None
    thread_id = request.session.get('thread_id', str(uuid.uuid4()))  # Retrieve or generate a unique thread ID
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Store the thread_id in the session if it's new
            if 'thread_id' not in request.session:
                request.session['thread_id'] = thread_id
            config = {"configurable": {"thread_id": thread_id}}
            user_query = form.cleaned_data['user_text']
            input_messages = [HumanMessage(user_query)]
            output = app.invoke(
                {"messages": input_messages}, config,
            )
            response=output["messages"][-1]
            # Clear the form after submission
            form = TextInputForm()
    return render(request, "learning/chatbot.html", {"form": form, "response": response})
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
    ner_text = None

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['user_text']
            action = request.POST.get('action')
            doc=nlp(user_text)

            if action == 'tokenize':
                tokenized_text = [token.text for token in doc]
            elif action == 'sentiment':
                blob = TextBlob(user_text)
                sentiment = blob.sentiment
            elif action == 'pos':
                pos = [token.pos_ for token in doc]
            elif action == 'ner':
                ner_text = [(entity.text, entity.label_) for entity in doc.ents] #[entity.label_ for entity in doc.ents]
            elif action == 'translate':
                #try:
                    detected_language = detect(user_text)
#                    translator = Translator()
                   # if detected_language == 'en':
 #                       translated_text = translator.translate(user_text,dest="tr")
                    #if detected_language == 'tr':
 #                       translated_text = translator.translate(user_text,dest="en")
                #except LangDetectException:
                    detected_language = "Language detection error. Please provide more text for detection."
                #except Exception as e:
                    detected_language = f"Translation Error: {e}"

    return render(request, 'learning/analyze_text.html', {
        'form': form,
        'user_text': user_text,
        'tokenized_text': tokenized_text,
        'sentiment': sentiment,
        'pos': pos,
        'detected_language': detected_language,
        'translated_text': translated_text,
        'ner_text': ner_text,
    })

