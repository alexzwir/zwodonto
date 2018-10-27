from django.shortcuts import render
from .forms import ContactForm, AppoinmentForm

# Create your views here.
def home(request):
    form = ContactForm()
    form_appoinment = AppoinmentForm()
    return render(request,"index.html",{"form":form,"form_appoinment":form_appoinment})