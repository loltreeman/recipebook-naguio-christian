from django import forms
from .models import Recipe, RecipeImage, Ingredient, RecipeIngredient
 
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class RecipeIngredientForm(forms.ModelForm):
    
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'