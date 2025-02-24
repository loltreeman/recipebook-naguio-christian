from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

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