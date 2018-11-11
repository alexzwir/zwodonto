from django import forms

class AppoinmentForm(forms.Form):
    appoinment_name = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome','size': '50','class':'form-control', 'name':'appoinment_name','type':'text','required':'required'}))
    appoinment_email = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu email','size': '50','class':'form-control','name':'appoinment_email','type':'email'}))
    appoinment_date = forms.CharField(max_length=50,label="",widget=forms.DateInput(attrs={'placeholder': 'Data da Consulta','size': '50','class':'form-control','id':'appoinment_date','name':'appoinment_date','type':'date'}))
    appoinment_phone = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu telefone','size': '50','class':'form-control','id':'appoinment_phone','name':'appoinment_phone','type':'text'}))
    appoinment_message = forms.CharField(max_length=50,label="",widget=forms.Textarea(attrs={'placeholder': 'Deixe sua mensagem','size': '50','class':'form-control required','name':'appoinment_message','rows':2}))

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome','size': '50','class':'form-control', 'name':'form_name','type':'text','required':''}))
    contact_email = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu email','size': '50','class':'form-control required email','name':'form_email','type':'email'}))
    contact_subject = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Escolha o assunto','size': '50', 'class':'form-control required', 'id':'form_subject','name':'form_subject','type':'text'}))
    contact_phone = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Digite seu telefone','size': '50','class':'form-control','id':'form_phone','name':'form_phone','type':'text'}))
    contact_message = forms.CharField(max_length=50,label="",widget=forms.Textarea(attrs={'placeholder': 'Deixe sua mensagem','size': '50','class':'form-control required','name':'form_message','rows':5}))