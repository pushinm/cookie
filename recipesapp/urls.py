from django.urls import path
from .views import (
    RecipeCreate, RecipeList, RecipeDetail, RecipeUpdate, RecipeDelete,
    CategoryCreate, CategoryList, CategoryDetail, CategoryUpdate, CategoryDelete,
    IngredientCreate, IngredientList, IngredientDetail, IngredientUpdate, IngredientDelete,
    InstructionCreate, InstructionList, InstructionDetail, InstructionUpdate, InstructionDelete,
)

urlpatterns = [
    # Recipe Endpoints
    path('recipes/create/', RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/update/<int:pk>/', RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/delete/<int:pk>/', RecipeDelete.as_view(), name='recipe-delete'),

    # Category Endpoints
    path('categories/create/', CategoryCreate.as_view(), name='category-create'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),

    # Ingredient Endpoints
    path('ingredients/create/', IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients/update/<int:pk>/', IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredients/delete/<int:pk>/', IngredientDelete.as_view(), name='ingredient-delete'),

    # Instruction Endpoints
    path('instructions/create/', InstructionCreate.as_view(), name='instruction-create'),
    path('instructions/', InstructionList.as_view(), name='instruction-list'),
    path('instructions/<int:pk>/', InstructionDetail.as_view(), name='instruction-detail'),
    path('instructions/update/<int:pk>/', InstructionUpdate.as_view(), name='instruction-update'),
    path('instructions/delete/<int:pk>/', InstructionDelete.as_view(), name='instruction-delete'),
]
