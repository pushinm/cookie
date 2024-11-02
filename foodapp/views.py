from rest_framework import serializers
from .models import Recipe, FoodLike, SaveRecipe, FoodComment, CommentLike, Category, Ingredient, Instruction
from userapp.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'photo')
        ref_name = 'UserProfile'

class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    recipe_likes_count = serializers.SerializerMethodField()
    recipe_comments_count = serializers.SerializerMethodField()
    me_liked = serializers.SerializerMethodField()
    me_saved = serializers.SerializerMethodField()
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "description",
            "image",
            "cook_time",
            "serves",
            "views_number",
            "location",
            "author",
            "categories",
            "created_at",
            "recipe_likes_count",
            "recipe_comments_count",
            "me_liked",
            "me_saved",
        )
        extra_kwargs = {"image": {"required": False}}

    def get_recipe_likes_count(self, obj):
        return obj.likes.count()

    def get_recipe_comments_count(self, obj):
        return obj.comments.count()

    def get_me_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return FoodLike.objects.filter(recipe=obj, author=request.user).exists()
        return False

    def get_me_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return SaveRecipe.objects.filter(recipe=obj, author=request.user).exists()
        return False

class FoodLikeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = FoodLike
        fields = ("id", "author", "recipe")

class SaveRecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = SaveRecipe
        fields = ("id", "author", "recipe")

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    me_liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = FoodComment
        fields = [
            "id",
            "author",
            "comment",
            "recipe",
            "parent",
            "created_at",
            "me_liked",
            "likes_count",
            "replies_count",
            "replies",
        ]

    def get_replies(self, obj):
        if obj.replies.exists():
            serializer = self.__class__(obj.replies.all(), many=True, context=self.context)
            return serializer.data
        return None

    def get_me_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.likes.filter(author=user).exists()
        return False

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_replies_count(self, obj):
        return obj.replies.count()

class CommentLikeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = ("id", "author", "comment")
