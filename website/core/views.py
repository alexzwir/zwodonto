from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, AppoinmentForm
from .models import AppoinmentModel
from django.utils import timezone


# Create your views here.
def home(request):
    form = ContactForm()
    form_appoinment = AppoinmentForm()
    return render(request,"index.html",{"form":form,"form_appoinment":form_appoinment})

def appoinment_saving(request):
    form_appoinment = AppoinmentForm(request.POST)
    if form_appoinment.is_valid():
        appoinment = AppoinmentModel(appoinment_name = form_appoinment.cleaned_data['appoinment_name'],
                                    appoinment_email = form_appoinment.cleaned_data['appoinment_email'],
                                    appoinment_date = form_appoinment.cleaned_data['appoinment_date'],
                                    appoinment_phone = form_appoinment.cleaned_data['appoinment_phone'],
                                    appoinment_message = form_appoinment.cleaned_data['appoinment_message'])
        appoinment.save()
    return HttpResponseRedirect('/')
