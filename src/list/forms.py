from django import forms
from.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            'title',
            'description',
            'date',
            'due_date',
            'done'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description':  forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'date': forms.SelectDateWidget(),
            'due_date': forms.DateTimeInput()
        }
