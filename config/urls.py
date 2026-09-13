
from django.contrib import admin
from django.urls import path, include

#http://127.0.0.1:8000/api/
urlpatterns = [
    path('api/', include('roles.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('spells.urls')),
]
 