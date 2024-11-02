from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint
from userapp.models import Users

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Null allows for "undeleted" instances

    class Meta:
        abstract = True  # Define as an abstract base model to avoid database table creation

class Recipe(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/recipes/')
    cook_time = models.PositiveIntegerField()  # Positive field to ensure valid values
    serves = models.PositiveIntegerField()
    views_number = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(Users, related_name='recipes', on_delete=models.CASCADE, verbose_name='Owner')
    categories = models.ManyToManyField('Category', related_name='recipes', verbose_name='Categories')

    def __str__(self):
        return self.title

class Instruction(BaseModel):
    recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
    text = models.TextField()
    images = models.ImageField(upload_to='media/instructions/')  # Use a JSON or Array field if multiple images needed

    def __str__(self):
        return self.text[:20]

class Ingredient(BaseModel):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)  # CharField with max length for concise ingredient text

    def __str__(self):
        return self.text[:20]

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)  # Unique constraint to avoid duplicate categories

    def __str__(self):
        return self.name

class FoodComment(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True
    )

    def __str__(self):
        return f"{self.comment[:20]} by {self.author}"

class FoodLike(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_food_like'
            )
        ]

    def __str__(self):
        return f"Like by {self.author} on {self.recipe}"

class CommentLike(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.ForeignKey(FoodComment, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'comment'],
                name='unique_comment_like'
            )
        ]

    def __str__(self):
        return f"Like by {self.author} on {self.comment}"

class SaveRecipe(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saves')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique_save_recipe'
            )
        ]

    def __str__(self):
        return f"Save by {self.author} on {self.recipe}"
