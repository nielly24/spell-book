from django.urls import path, include

urlpatterns = [
    path('api/', include('roles.urls')),
    path('api/', include('accounts.urls')),
    path('api/shop/', include('shop.urls')), 
]