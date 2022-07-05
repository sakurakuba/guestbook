from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='author')
    email = forms.EmailField(max_length=254, required=True, label='email')
    content = forms.CharField(max_length=3000, required=True, label='content', widget=widgets.Textarea(attrs={"cols": 20, "rows": 2}))
