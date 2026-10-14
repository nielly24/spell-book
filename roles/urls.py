from django.urls import path
from roles.views import RoleListView,RoleCreateView, RoleDetailView

#http://localhost:8000/api/roles
#http://localhost:8000/api/roles<id>
urlpatterns = [
    path('roles/', RoleListView.as_view()),
    path('roles/new/', RoleCreateView.as_view()),
    path('roles/<int:pk>/', RoleDetailView.as_view())
]