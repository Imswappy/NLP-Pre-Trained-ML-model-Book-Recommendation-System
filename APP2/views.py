from django.shortcuts import render
from .forms import DataForm
from django.contrib import messages
from .import models

def index(request):
    message=models.MessageToForm.objects.all().order_by('-id')[:1]
    if request.method=="POST":
        form=DataForm(request.POST or None,request.FILES)
        
        #incase form is validated
        
        if form.is_valid():
            form.save()
            messages.success(request,"You have successfully registered")
            #clear the form
            form=DataForm()
            return render(request,'index.html',{'form':form,'ujumbe':message,})
        else:
            return render(request,'index.html',{'form':form,'ujumbe':message,})
        #if form is not submitted
    else:
        form=DataForm()
        return render(request,'index.html',{'form':form,'ujumbe':message,})
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return render(request,'index.html')