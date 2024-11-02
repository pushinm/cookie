from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from foodapp.models import Recipes, Category, Ingredients, Instructions
from .serializers import RecipesSerializer, CategorySerializer, IngredientSerializer, InstructionSerializer

# Generalized view class to avoid repetition
class BaseCreateView(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)

class BaseUpdateView(generics.UpdateAPIView):
    parser_classes = (FormParser, MultiPartParser)

# Recipe Views
class RecipeCreate(BaseCreateView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipeList(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipeUpdate(BaseUpdateView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class RecipeDelete(generics.DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

# Category Views
class CategoryCreate(BaseCreateView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdate(BaseUpdateView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Ingredient Views
class IngredientCreate(BaseCreateView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class IngredientList(generics.ListAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class IngredientUpdate(BaseUpdateView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class IngredientDelete(generics.DestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

# Instruction Views
class InstructionCreate(BaseCreateView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer

class InstructionList(generics.ListAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer

class InstructionDetail(generics.RetrieveAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer

class InstructionUpdate(BaseUpdateView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer

class InstructionDelete(generics.DestroyAPIView):
    queryset = Instructions.objects.all()
    serializer_class = InstructionSerializer
