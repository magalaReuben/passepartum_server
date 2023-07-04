import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from passepartum_translation.services.translation import model


@csrf_exempt
def translate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            language = data.get('language')
            text_list = data.get('text')
            translated = []
            for text in text_list:
                # Translate a sentence
                translation = model.translate(text)
                translated.append(translation)
            return JsonResponse({'original':text_list, 'translation': translated})
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)
