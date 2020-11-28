from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime
# Create your views here.
def main(request):
    return render(request, 'main.html', {'parameter': "test"})

def health(request):
    response = {'date': datetime.now(), 'current_page': request.build_absolute_uri(), 'Info_server': os.name, 'client_info': request.headers['User-Agent']}
    return JsonResponse(response)
