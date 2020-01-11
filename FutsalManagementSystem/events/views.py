from django.shortcuts import render
from .models import Event
from django.http import HttpResponse

# Create your views here.
def view_event_data(request):
    events_list=Event.objects.all()
    con_var={
        'events':events_list
    }
    return render(request,'event/viewevent.html',con_var)

def view_event_form(request):
    return render(request,'event/save_event.html')