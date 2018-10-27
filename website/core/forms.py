from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome','size': '50','class':'form-control', 'name':'form_name','type':'text','required':''}))
    contact_email = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu email','size': '50','class':'form-control required email','name':'form_email','type':'email'}))
    contact_subject = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Escolha o assunto','size': '50', 'class':'form-control required', 'id':'form_subject','name':'form_subject','type':'text'}))
    contact_phone = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu telefone','size': '50','class':'form-control','id':'form_phone','name':'form_phone','type':'text'}))
    contact_message = forms.CharField(max_length=50,label="",widget=forms.Textarea(attrs={'placeholder': 'Deixe sua mensagem','size': '50','class':'form-control required','name':'form_message','rows':5}))


"""
contact_name = models.CharField(max_length=30)
contact_email = models.CharField(max_length=30)
contact_phone = models.CharField(max_length=30)
contact_subject = models.CharField(max_length=30)
contact_message = models.CharField(max_length=30)
contact_sent_date = models.DateTimeField(max_length=35,default=timezone.now)
"""