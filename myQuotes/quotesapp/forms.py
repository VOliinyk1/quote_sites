from django.contrib.postgres.fields import ArrayField
from django.db.models import ForeignKey
from django.forms import ModelForm, TextInput, CharField, IntegerField, ModelChoiceField, Select
from django.db import models

from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=17, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=250, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    tags = ArrayField(base_field=CharField(max_length=30), max_length=20)
    quote = CharField(max_length=250, widget=TextInput(attrs={"class": "form-control"}))
    author = ModelChoiceField(queryset=Author.objects.all(), widget=Select)

    class Meta:
        model = Quote
        fields = ['tags', 'quote', 'author']

