from django.urls import path
from categories.views import * 

urlpatterns = [
    path('categories/', CategoriesListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view())
]