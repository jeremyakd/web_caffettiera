from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categories/<int:category_id>/', views.categories, name="categories"),
]

