from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient, RecipeIngredient

# So I want to display a list for all the recipe objects
# I don't know what to do AHHHHHHHHH
# I think you make views like actually now instead of the request type shi
# so like instead of return render(req) type, you actuallly make object name for that bruhh
# TODO: maybe make like context obj name and like make a way to substitute the request render and just refer ing and rep

class RecipeListView(ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'
    
class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'recipeDetails.html'
    context_object_name = 'recipe'

def populateDatabase(request):

    recipe1, _ = Recipe.objects.get_or_create(name="Recipe 1")

    tomato, _ = Ingredient.objects.get_or_create(name="tomato")
    onion, _ = Ingredient.objects.get_or_create(name="onion")
    pork, _ = Ingredient.objects.get_or_create(name="pork")
    water, _ = Ingredient.objects.get_or_create(name="water")
    sinigang_mix, _ = Ingredient.objects.get_or_create(name="sinigang mix")

    RecipeIngredient.objects.get_or_create(recipe=recipe1, ingredient=tomato, quantity="3pcs")
    RecipeIngredient.objects.get_or_create(recipe=recipe1, ingredient=onion, quantity="1pc")
    RecipeIngredient.objects.get_or_create(recipe=recipe1, ingredient=pork, quantity="1kg")
    RecipeIngredient.objects.get_or_create(recipe=recipe1, ingredient=water, quantity="1L")
    RecipeIngredient.objects.get_or_create(recipe=recipe1, ingredient=sinigang_mix, quantity="1 packet")

    recipe2, _ = Recipe.objects.get_or_create(name="Recipe 2")

    garlic, _ = Ingredient.objects.get_or_create(name="garlic")
    vinegar, _ = Ingredient.objects.get_or_create(name="vinegar")
    salt, _ = Ingredient.objects.get_or_create(name="salt")
    black_peppers, _ = Ingredient.objects.get_or_create(name="whole black peppers")

    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=garlic, quantity="1 head")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=onion, quantity="1pc")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=vinegar, quantity="1/2cup")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=water, quantity="1 cup")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=salt, quantity="1 tablespoon")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=black_peppers, quantity="1 tablespoon")
    RecipeIngredient.objects.get_or_create(recipe=recipe2, ingredient=pork, quantity="1 kilo")

    recipes = Recipe.objects.all()
    return render(request, "recipeList.html", {"recipes": recipes})


