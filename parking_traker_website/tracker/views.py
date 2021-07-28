from django.shortcuts import render
from django.http import JsonResponse
from .refresh import *

# Create your views here.
def main_view(request):
    if request.method == 'POST' and request.is_ajax():
        print("ajax is called")
        index =  int(request.POST.get('index'))
     
        cur = get_count(index)
        return JsonResponse({'count':cur})
    
    
    total = 12
    current = -1
    available = -1
    context = {
        'total': total,
        'current': current,
        'available': available        
    }
    return render(request, 'main.html',context)

