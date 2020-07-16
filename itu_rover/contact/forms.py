from django.forms import ModelForm, Textarea
from .models import ContactForm_model

class ContactForm(ModelForm):
    class Meta:
        model = ContactForm_model

        #fields = '__all__'

        exclude = ['date']

        widgets = {
            'text': Textarea(attrs={"width": "100%"}),


        }
