from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeListView(ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'
    
class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'recipeDetail.html'
    context_object_name = 'recipe'