from django.urls import path

from spells.views import *

urlpatterns = [
    path('spells/', SpellListCreateView.as_view()),
    path('spells/<int:pk>/', SpellDetailView.as_view())
]