from django.urls import path
from .views import*

urlpatterns = [
    path('', Home.as_view(), name="blog"),
    path('<int:pk>/', detail, name="blog-detail"),
    path('category/<category>/', category, name="blog-category")
]