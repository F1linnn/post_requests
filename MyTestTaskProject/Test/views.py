from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import find_matching_template, get_types_form
import requests 

from tinydb import TinyDB

db = TinyDB('db.json')

@csrf_exempt
def get_form(request):
    if request.method == 'POST':
        form_data = request.POST.dict()

        form_templates = db.table("Form_templates").all()

        matching_template = find_matching_template(form_data, form_templates)

        if matching_template:
            return JsonResponse({"template_name": matching_template['FormName']})
        else:
            field_types = get_types_form(form_data)
            return JsonResponse(field_types)
        
    else:
        return JsonResponse({"400 Bad request": "Only POST request"})