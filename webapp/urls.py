from django.urls import path
from .views import*

urlpatterns = [
    path('', Home, name="index"),
    path('portfolio/', Portfolio.as_view(), name="portfolio"),
    path('<int:pk>/', Detail.as_view(), name="detail"),
    path('<str:name>/', category, name="category"),
    path('contact', contact, name="contact")
]