from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import formsclass
from .models import madhan #user class names from models.py


class class1(ListView):
    model = madhan

class class2(DetailView):
    model = madhan
    fields = "__all__"
    
class class3(CreateView):                      
    model = madhan 
    formclass = formsclass
    #feilds must be same model variables
    fields = ['news', 'add_image', 'video', 'status', 'place']
    success_url = reverse_lazy('mm_list')

def termsandconditions(request):
    return render(request, 'termsandconditions.html')

def policy(request):
    return render(request, 'policy.html')
   
def pageinpage(request):
    return render(request, 'pageinpage.html')
