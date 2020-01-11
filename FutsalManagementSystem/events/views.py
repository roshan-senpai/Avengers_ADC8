from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context
from .models import Event

# view function for updating page
def view_update_page(request):
    return render(request,'events/update.html')

# view function for listing event data page
def view_eventdata_updateform(request,ID):
    # print(ID)
    event_obj = Event.objects.all()
    print(event_obj)
    context_varible = {
        'event':event_obj
    }
    return render(request,'events/eventdataform.html',context_varible)

# view function for updating in the database page
def view_update_form_data_in_db(request,ID):
    event_obj = Event.objects.get(id=ID)
    print(event_obj)
    event_form_data = request.POST
    print(event_form_data)
    event_obj.event_name = request.POST['event_name']
    event_obj.venue =request.POST['venue']
    event_obj.event_date = request.POST['event_date']
    event_obj.manager = request.POST['manager']
    event_obj.save()

    return HttpResponse("Record Updated!!")