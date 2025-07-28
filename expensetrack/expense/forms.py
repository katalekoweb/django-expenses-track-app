from django import forms 
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'p-2 border border-gray-200 block w-full rounded-md shadow-md'}),
            'amount': forms.NumberInput(attrs={'class': 'p-2 border border-gray-200 block w-full rounded-md shadow-md'}),
            'description': forms.Textarea(attrs={'class': 'p-2 border border-gray-200 block w-full rounded-md shadow-md', 'rows': 3}),
        }
    
    # def clean_amount(self):
    #     amount = self.cleaned_data.get('amount')
    #     if amount <= 0:
    #         raise forms.ValidationError("Amount must be greater than zero.")
    #     return amount