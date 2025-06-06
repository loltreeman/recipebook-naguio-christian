from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient
from django.urls import reverse_lazy, reverse
from . import models, forms
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm
class RecipeListView(LoginRequiredMixin, ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'
    
class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    template_name = 'recipeDetail.html'
    context_object_name = 'recipe'
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    form_class = RecipeForm  
    template_name = 'recipeAdd.html'
    success_url = reverse_lazy("ledger:recipe_add")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_form'] = IngredientForm()
        context['recipe_ingredient_form'] = RecipeIngredientForm()
        return context
    
    def form_valid(self, form):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)
class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeIngredientForm
    template_name = 'recipeAdd.html'  

    def form_valid(self, form):
        form.save()
        return redirect('ledger:recipe_add')  

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_add')

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = models.RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipeCreate.html'

    def form_valid(self, form):
        recipe = get_object_or_404(models.Recipe, pk=self.kwargs['pk'])
        recipe_image = form.save(commit=False)
        recipe_image.recipe = recipe
        recipe_image.save()
        return redirect('ledger:recipe_detail', pk=recipe.pk) 

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_detail',
            kwargs={'pk': self.kwargs['pk']}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(
            models.Recipe, pk=self.kwargs['pk']
        )
        return context

class RecipeAddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'recipeAddIngredient.html'

    def get_success_url(self):
        return reverse("ledger:recipe_add")