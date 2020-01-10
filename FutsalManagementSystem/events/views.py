from django.shortcuts import render

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match = Event.objects.filter(Q(event_name__icontains=srch) |
                                         Q(venue__icontains=srch)
                                         )
            if match:
                return render(request,'searchdata.html', {'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'searchdata.html')

# Create your views here.

