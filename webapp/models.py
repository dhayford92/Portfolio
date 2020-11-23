from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title