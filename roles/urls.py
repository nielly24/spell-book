from django.urls import path
from roles.views import RoleListCreateView, RoleDetailView
#http://localhost:8000/api/roles
#http://localhost:8000/api/roles<id>
urlpatterns = [
    path('roles/', RoleListCreateView.as_view()),
    path('roles/<int:pk>/', RoleDetailView.as_view())
]