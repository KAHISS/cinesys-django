from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Critic(models.Model):
    movie_id = models.CharField(max_length=100, verbose_name="Movie ID")
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    poster_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
