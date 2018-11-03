from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, AppoinmentForm
from .models import AppoinmentModel,ContactModel
from django.utils import timezone


# Create your views here.
def home(request):
    form = ContactForm()
    form_appoinment = AppoinmentForm()
    return render(request,"index.html",{"form_appoinment":form_appoinment,"form":form})

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

def sending_message(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = ContactModel(contact_name = form.cleaned_data['contact_name'],
                                contact_email = form.cleaned_data['contact_email'],
                                contact_phone = form.cleaned_data['contact_phone'],
                                contact_subject = form.cleaned_data['contact_subject'],
                                contact_message = form.cleaned_data['contact_message'])
        contact.save()
    return HttpResponseRedirect('/')
