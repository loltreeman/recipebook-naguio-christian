from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),  
    path('logout/', LogoutView.as_view(), name="logout"),  
    path('recipes/list/', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipes/add', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image/', views.RecipeImageCreateView.as_view(), name='recipe_add_image'),
    path('recipes/add/ingredient/', views.RecipeAddIngredientView.as_view(), name='recipe_add_ingredient'),
    path('recipes/add/recipe-ingredient/', views.RecipeIngredientCreateView.as_view(), name='recipe_ingredient_add'),
]

app_name = "ledger"
