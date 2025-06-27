from django.contrib import admin
from .models import Critic, Category


@admin.register(Critic)
class CriticAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
