from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    link = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(Category, default='uncategorize')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    number = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class AddProfileImage(models.Model):
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)