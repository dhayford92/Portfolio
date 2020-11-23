from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name="index"),
    path('portfolio/', portfolio, name="portfolio"),
    path('detail/<int:pk>/', detail, name="detail"),
    path('category/<str:cats>/', category, name="category")
]