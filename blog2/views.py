from django.shortcuts import render,redirect
from .models import *
from .forms import Employee_form
from django.http import *
from django.urls import reverse
from django.db.models import Q
def home(request):
        
   if request.method=='POST':
        form=Employee_form(request.POST)
        if form.is_valid():
             form.save()
             return display(request)
             #return HttpResponseRedirect('/Employee_form/')
    
   else:
        form=Employee_form()
   return render(request,'blog2/register.html',{'form':form})
   
def display(request):
     obj=Employee.objects.all()
     return render(request, 'blog2/display.html' ,{'obj':obj})

def search(request):
       if request.method =='GET':
           srch=request.GET.get['srh']
           if srch:
               match=Employee.objects.filter(Q(name_icontains=srch))
              
               if match:
                   return render(request,'blog2/search.html',{'sr':match})
               else:
                    return render(request, 'blog2/search.html')
        else:
            return render(request, 'blog2/search.html')
        return render(request, 'blog2/search.html')