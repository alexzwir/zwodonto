from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

SOURCE_CHOICES = (
    ("indicacao_paciente","Indicação paciente"),
    ("mídia","Mídia"),
    ("indicacao_medica","Indicação médica"),
    ("indicacao_odonto","Indicação odontológica"),
)

class PatientModel(models.Model):
    patient_name = models.CharField(verbose_name="Nome",max_length=120,unique=True)
    patient_created_date = models.DateTimeField(verbose_name="Data de Incrição",auto_now=False,auto_now_add=False, default=timezone.now,editable=True)
    patient_updated_date = models.DateTimeField(auto_now=True,auto_now_add=False,editable=True)
    patient_email = models.EmailField(verbose_name="Email",max_length=120, unique=True)
    patient_source = models.CharField(verbose_name="Indicação",max_length=120,choices=SOURCE_CHOICES, default="indicação")
    patient_phone = models.CharField(verbose_name="Telefone",max_length=120)
    patient_phone_backup = models.CharField(verbose_name="Telefone 2",max_length=120)
    patient_address = models.CharField(verbose_name="Endereço",max_length=120,null=True)
    patient_active = models.BooleanField(verbose_name="Status do Paciente",default=True)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
    
    def __str__(self):
        return smart_text(self.patient_name)