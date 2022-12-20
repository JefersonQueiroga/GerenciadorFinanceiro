from django import forms
from django.forms import ModelForm, inlineformset_factory

from apps.transactions.models import Transaction


class TransactionForm(ModelForm):
       
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Transaction
        fields = ["description", "type_operation", "form_payment", "category","date_transaction",]
        
        widgets = {
            'date_transaction': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    
        
    