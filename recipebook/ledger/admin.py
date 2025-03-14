from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
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

class RecipeIngredientAdmin(admin.ModelAdmin):
    
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')  
    list_filter = ('recipe', 'ingredient')  
    search_fields = ('recipe__name', 'ingredient__name') 

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
