from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'
    
class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    template_name = 'recipeDetail.html'
    context_object_name = 'recipe'