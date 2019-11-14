from django.shortcuts import render, HttpResponseRedirect, reverse


from django.contrib.auth import login, logout, authenticate

from RecipeBoxV1.models import RecipeItem, Author
from RecipeBoxV1.forms import RecipeItemAddForm, AuthorAddForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    html = 'index.html'
    data = RecipeItem.objects.all()
    return render(request, html, {'data': data})


def login_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user:= authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )

    form = LoginForm()

    return render(request, html, {'form': form}


def logout_view(request):



def read_recipe(request, id):
    recipe_html = "recipes.html"
    recipe_data = RecipeItem.objects.filter(id=id)
    return render(request, recipe_html, {'data': recipe_data})


def author_view(request, id):
    author_html = 'authors.html'
    author = Author.objects.filter(id=id)
    recipes = RecipeItem.objects.filter(author=id)

    return render(request, author_html, {'data': author, 'recipes': recipes})


@login_required
def authoraddview(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})


@login_required
def recipeaddview(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = RecipeItemAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                author=data['author'],
                title=data['title'],
                body=data['body'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeItemAddForm()


    return render(request, html, {'form': form})
    print()


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse)('homepage')
