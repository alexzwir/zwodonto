from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

# Create your models here.

class ContactModel(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=30)
    contact_subject = models.CharField(max_length=30)
    contact_message = models.CharField(max_length=30)
    contact_sent_date = models.DateTimeField(max_length=35,default=timezone.now)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return smart_text("{} | {} | {}".format(self.contact_name,self.contact_sent_date,self.contact_email))
