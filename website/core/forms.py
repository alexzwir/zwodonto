from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome','size': '50',"class":"form-control"}))
    contact_email = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu email','size': '50',"class":"form-control"}))
    contact_phone = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu telefone','size': '50',"class":"form-control"}))
    contact_subject = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Escolha o assunto','size': '50',"class":"form-control"}))
    contact_message = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Deixe sua mensagem','size': '50',"class":"form-control"}))

"""
contact_name = models.CharField(max_length=30)
contact_email = models.CharField(max_length=30)
contact_phone = models.CharField(max_length=30)
contact_subject = models.CharField(max_length=30)
contact_message = models.CharField(max_length=30)
contact_sent_date = models.DateTimeField(max_length=35,default=timezone.now)
"""