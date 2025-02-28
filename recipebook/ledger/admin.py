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

class IngredientAdmin(admin.ModelAdmin):
    
    model = Ingredient 
    list_display = ('name', )
    search_fields = ('name',  )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
