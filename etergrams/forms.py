from django import forms
from .models import Tag
from .models import Entry
#from .models import Entry

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'photo']
        labels = {'text': '', 'photo': 'select a file'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
