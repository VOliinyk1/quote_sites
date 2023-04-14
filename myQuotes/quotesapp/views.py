import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json

from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
from django.conf import settings


# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/quotes.html', context={'title': 'myQuotes',
                                                             'quotes': quotes})


@login_required
def load_data(request):
    filepaths = ['authors.json', 'quotes.json']

    if len(Quote.objects.all()) < 100:

        with open(os.path.join(settings.STATIC_ROOT, filepaths[0])) as f:
            authors_data = json.load(f)

        with open(os.path.join(settings.STATIC_ROOT, filepaths[1])) as f:
            quotes_data = json.load(f)

        for item in authors_data:
            authors = Author(
                fullname=item['fullname'],
                born_date=item['born_date'],
                born_location=item['born_location'],
                description=item['description']
            )
            authors.save()

        for item in quotes_data:
            print(item['author'])
            quotes = Quote(
                tags=item['tags'],
                author=Author.objects.get(fullname=item['author']),
                quote=item['quote'][:250]
            )
            quotes.save()
        return redirect(to='quotesapp:root')

    return redirect(to='quotesapp:root')


def show_author(request, auth_id):
    author = Author.objects.filter(pk=auth_id).first()
    print(author)
    return render(request, 'quotesapp/author.html',
                  context={"title": f"{author.fullname}",
                           "author": author})


@login_required
def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:root')

    return render(request, 'quotesapp/new_author.html',
                  context={"title": f"title",
                           "form": form})


@login_required
def add_quote(request):
    form = QuoteForm()
    authors = Author.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            qt_form = form.save(commit=False)
            print(qt_form)
            qt_form.tags = qt_form.tags[0].split(' ')

            qt_form.save()
            return redirect(to='quotesapp:root')

    return render(request, 'quotesapp/new_quote.html', context={'form': form})
