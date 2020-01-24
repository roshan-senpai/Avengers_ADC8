from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.template import Template,Context


# Create your views here.
def view_event_data(request):
    events_list=Event.objects.all()
    con_var={
        'events':events_list
    }
    return render(request,'event/viewevent.html',con_var)

def view_event_form(request):
    return render(request,'event/save_event.html')
    
def view_event_save(request):
    if request.method == "POST":
        get_name=request.POST['event_name']
        get_venue=request.POST['event_venue']
        get_date=request.POST['event_date']
        get_manager=request.POST['event_manager']
        Event.objects.create(event_name=get_name,venue=get_venue,event_date=get_date,manager=get_manager)
        return HttpResponse("Added Sucessfully")    
    else:
        return HttpResponse("Error while adding") 

def view_event_delete(request,ID):
    print(ID)
    event_obj=Event.objects.get(id=ID)
    con_var={
        'event':event_obj
    }
    event_obj.delete()
    return render(request,'event/delete_data.html',con_var)
    

# view function for updating page
def view_update_page(request):
    return render(request,'events/update.html')

# view function for listing event data page
def view_eventform(request,ID):
    print(ID)
    event_obj = Event.objects.get(id=ID)
    print(event_obj)
    context_varible = {
        'event':event_obj
    }
    return render(request,'events/eventdataupdateform.html',context_varible)

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
    return HttpResponse("            Record Updated!!")


# view function for searhing in the database page
def view_search_data(request,ID):
    print(ID)
    event_obj = Event.objects.get(id=ID)
    print(event_obj)
    context_varible = {
        'event':event_obj
    }
    return render(request,'events/searchdata.html',context_varible)
    # if request.method=='POST':
    #     search=request.POST['srh']
    #     if search:
    #         match=Event.objects.filter(event_name__icontains=search)

    #         if match:
    #             return render(request,'search.html',{'sr':match})

    #         else:
    #             return HttpResponse('NO EVENT FOUND!')
                       
    #     else:
    #         return HttpResponse('ENTER EVENT NAME!!')

    # else:
    #     return render(request,'searchdata.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        file_object = FileSystemStorage()
        file_object.save(uploaded_file.name, uploaded_file)
    return render(request,'upload.html')

