from django.shortcuts import render
from django.http import JsonResponse
from .refresh import *
from datetime import datetime
import time as ti
from .models import *
import json

# Create your views here.
def main_view(request):
    if request.method == 'POST' and request.is_ajax():
        #print("ajax is called")
        #index =  int(request.POST.get('index'))
     
        cur = get_count()
        time = datetime.fromtimestamp(ti.time()).strftime("%H:%M:%S")
        new_count = Car_Count(time = time, count = cur)
        new_count.save()
        request.session['current_count'] = cur
        request.session['current_time'] = time
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

def graph_view(request):
    if request.method == 'POST' and request.is_ajax():
        return JsonResponse({'current_count': request.session['current_count'], 
                             'current_time': request.session['current_time'],
                            })
    
    latest_ten_count = Car_Count.objects.all().order_by('-time')[:10]
    count_data = list(latest_ten_count.values_list('count', flat = True))[::-1]
    time_data = json.dumps(list(latest_ten_count.values_list('time', flat =True))[::-1])
    
    context = {
        'count_data': count_data,
        'time_data': time_data,
    }
    return render(request, 'graph.html', context)

def convertTime(unixTime):
    return datetime.fromtimestamp(unixTime).strftime("%H:%M:%S")