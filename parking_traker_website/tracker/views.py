from django.shortcuts import render
from django.http import JsonResponse
from .refresh import *

# Create your views here.
def main_view(request):
    if request.method == 'POST' and request.is_ajax():
        print("ajax went through is called")
        new_image()
        return JsonResponse({})
    return render(request, 'main.html',{})

