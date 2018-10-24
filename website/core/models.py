from django.db import models

# Create your models here.

class ContactModel(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=30)
    contact_subject = models.CharField(max_length=30)
    contact_message = models.CharField(max_length=30)