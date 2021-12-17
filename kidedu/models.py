from django.db import models
from django.contrib.auth.models import User


# Articles
class Article(models.Model):
    title = models.CharField(max_length=200, blank="False", null="False")
    image = models.ImageField(blank="False", null="False")
    description = models.TextField(blank="False", null="False")
    date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=500, blank='False', null='False')

    def __str__(self):
        return self.title


# Comments
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} | {self.body}"


# colors game
class Colors(models.Model):
    title = models.CharField(max_length=200, blank="False", null="False")
    image = models.ImageField(blank="False", null="False")
    sentence = models.TextField(blank="False", null="False")
    color = models.CharField(blank="False", null="False", max_length=64)

    def __str__(self):
        return self.title
