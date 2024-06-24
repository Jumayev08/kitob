# library_project/library_app/forms.py
from django import forms
from .models import Book

class BookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Select a Book")
