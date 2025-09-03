from django.shortcuts import render
from . import models

from django.shortcuts import render,redirect
from .forms import DataForm
from django.http import HttpResponseRedirect
from django.contrib import messages

#import registration class
from APP2.models import Registration as registration
#return home.html

def home(request):
    anouncement=models.Announcements.objects.all().order_by('-id')[:4]
    programs=models.Programs.objects.all().order_by('-program_name')[:10]
    best=models.Herroes.objects.all().order_by('-id')[:1]
    return render(request,'home.html',{'announcements':anouncement,'programs':programs,'best':best})

def herroes(request):
    best=models.Herroes.objects.all().order_by('-id')
    return render(request,'herroes.html',{'best':best})

def about(request):
    return render(request,'about.html')

def anouncements(request):
    anouncement=models.Announcements.objects.all().order_by('-id')
    return render(request,'anouncements.html',{'announcements':anouncement})

def courses(request):
    programs=models.Programs.objects.all().order_by('-program_name')
    return render(request,'courses.html',{'programs':programs})

def appstatus(request):
    frequency=registration.objects.all().count()
    applicants=registration.objects.all().order_by('created_at')[:1000]
    needed=1000
    return render(request,'status.html',{'applicants':applicants
                                   ,'frequency':frequency,
                                   'needed':needed,
                                   'applicants_percentage':  round(((frequency/needed)*(100)),2),
                                   'remaining_position_percentage':round(((needed-frequency)/(needed)*(100)),2),
                                   'range':needed-frequency})
 


def application(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully")
            #return HttpResponseRedirect('/')
            return redirect('application')
        else:
            messages.error(request,"Failed")
    else:
         form = DataForm()
         context = {
        'form': form,}
    return render(request, 'application.html', context)


