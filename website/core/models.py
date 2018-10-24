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
        raw_data = str(self.contact_sent_date)
        normalized_data = raw_data[0:10]
        day_normalized = normalized_data[8:10]
        month_normalized = normalized_data[5:7]
        new_date_normalied = day_normalized + "/" +month_normalized
        return smart_text("{} | {} | {}").format(self.contact_name, new_date_normalied, self.contact_email)
