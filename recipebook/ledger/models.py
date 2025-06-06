from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.TextField(max_length=50, blank=True)
    user_bio = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk': self.pk})
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Image for {self.recipe.name}"

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.recipe.pk)])

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, related_name = "recipe")
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "ingredients")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args = [str(self.recipe.pk)])