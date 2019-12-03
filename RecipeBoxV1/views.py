from django.shortcuts import render, HttpResponseRedirect, reverse


from django.contrib.auth import login, logout, authenticate

from RecipeBoxV1.models import RecipeItem, Author
from RecipeBoxV1.forms import RecipeItemAddForm, AuthorAddForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    html = 'index.html'
    data = RecipeItem.objects.all()

    if request.user.is_authenticated:
        button_href = '/logout/'
        button_display = 'LOGOUT'
    else:
    # Do something for anonymous users.
        button_href = 'login/'
        button_display = 'LOGIN'

    return render(request, html, {'data': data})


def read_recipe(request, id):
    recipe_html = "recipes.html"
    recipe_data = RecipeItem.objects.filter(id=id)
    return render(request, recipe_html, {'data': recipe_data})

@login_required
def author_view(request, id):
    author_html = 'author.html'
    author = Author.objects.filter(id=id).first()
    recipes = RecipeItem.objects.filter(author=id)
    favorites = author.favorites.all()


    return render(request, author_html, {'author': author, 'recipes': recipes, 'favorites': favorites})


@login_required
def addauthorview(request):
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

def favorite_recipe(request, id):
    currentuser = request.user.author
    recipe = RecipeItem.objects.get(id=id)
    currentuser.favorites.add(recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unfavorite_recipe(request, id):
    currentuser = request.user.author
    recipe = RecipeItem.objects.get(id=id)
    currentuser.favorites.remove(recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def recipe_edit_view(request, id):
    html = "generic_form.html"
    user_author = request.user
    instance = RecipeItem.objects.get(id=id)
    form = RecipeItemAddForm(request.POST or None, instance=instance)

    if form.is_valid():
        if user_author.is_staff or user_author == instance.author.user:
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = RecipeItemAddForm(instance=instance)

    return render(request, html, {'form': form})
        
def login_view(request):
    html = 'generic_form.html'
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', '/')
                )
    return render(request, html, {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
