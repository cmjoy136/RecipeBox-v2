"""
Author
    Name
RecipeItem
    Date
    Title
    Body
    author
"""
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateTimeField()
    time_required = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"