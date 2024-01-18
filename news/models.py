# news/models.py
from django.db import models
from .validators import validate_title_words


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title_words])
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
