from django.db import models

class Category(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=250)


class Blog(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=250)
    body = models.TextField()
    categories = models.ManyToManyField('Category', related_name='posts', blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.CharField(max_length=250)
    body = models.TextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)