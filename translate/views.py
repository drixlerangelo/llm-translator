from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from langchain_openai import ChatOpenAI
from langchain_community.llms.ollama import Ollama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.chat import ChatPromptTemplate
from app import settings
import re

def show(request: HttpRequest) -> JsonResponse:
    if 'text' not in request.GET.keys():
        return JsonResponse({
            'data': None,
            'message': 'Nothing to translate.',
            'success': False,
        })

    supported_langs = {
        'en': 'English',
        'jp': 'Japanese',
        'fr': 'French',
        'es': 'Spanish',
    }

    source_lang = request.GET['sl'] if 'sl' in request.GET.keys() else None
    target_lang = request.GET['tl'] if 'tl' in request.GET.keys() else None

    if settings.LLM_TYPE == 'google':
        supported_langs['tl'] = 'Filipino' # Doesn't work on other LLMs.
        chat_model = ChatGoogleGenerativeAI(google_api_key=settings.LLM_KEY, model=settings.LLM_NAME, convert_system_message_to_human=True)
    elif settings.LLM_TYPE == 'openai':
        chat_model = ChatOpenAI(openai_api_key=settings.LLM_KEY, model_name=settings.LLM_NAME)
    else:
        chat_model = Ollama(model=settings.LLM_NAME, base_url=settings.LLM_URL)

    if source_lang not in supported_langs.keys():
        return JsonResponse({
            'data': None,
            'message': 'Source language not supported.',
            'success': False,
        })

    if target_lang not in supported_langs.keys():
        return JsonResponse({
            'data': None,
            'message': 'Target language not supported.',
            'success': False,
        })

    system_template = "You are a helpful assistant that translates {input_language} to {output_language}."
    human_template = "Translate the text below and don't show any other response: \n{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ('system', system_template),
        ('human', human_template),
    ])

    messages = chat_prompt.format_messages(
        input_language=supported_langs[source_lang],
        output_language=supported_langs[target_lang],
        text=re.sub(r'\s+', ' ', request.GET['text'].strip())
    )

    try:
        result = chat_model.invoke(messages)

        return JsonResponse({
            'data': result if type(result) == str else result.content,
            'message': 'Translation complete.',
            'success': True,
        })
    except:
        return JsonResponse({
            'data': None,
            'message': 'Translation unsuccessful. Please try again later.',
            'success': False,
        })

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

