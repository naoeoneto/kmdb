from rest_framework import serializers
from reviews.models import Review
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        read_only_fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    stars = serializers.IntegerField(validators=[
        MinValueValidator(1, message='Ensure this value is greater than or equal to 1.'), 
        MaxValueValidator(5, message='Ensure this value is less than or equal to 5.')]
        )
    critic = CriticSerializer(many=False, read_only=True)
    
    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "movie_id", "critic"]
        read_only_fields = ["id", "movie_id", "critic"]
        extra_kwargs = {"stars": {"required": True}, "review": {"required": True}, "critic": {"required": True}}
