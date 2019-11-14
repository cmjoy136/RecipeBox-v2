"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
# from RecipeBoxV1 import views
from RecipeBoxV1.models import Author, RecipeItem
# from django.conf import settings
# from django.conf.urls.static import static

from RecipeBoxV1.views import index, read_recipe, recipeaddview, authoraddview
from RecipeBoxV1.views import login_view, logout_view


admin.site.register(Author)
admin.site.register(RecipeItem)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    # path('recipes/<int:id>/', read_recipe, name='recipe_list'),
    # path('authors/<int:id>/', views.authors_info, name='authors_page'),

    path('addrecipe/', recipeaddview),
    path('addauthor/', authoraddview),
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout')

]
