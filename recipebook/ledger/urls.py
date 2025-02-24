from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name="recipe_list"),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
]