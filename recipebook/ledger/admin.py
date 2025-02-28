from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', )  
    search_fields = ('name', )  
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)