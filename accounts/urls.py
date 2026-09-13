from django.urls import path

from accounts.views import *

urlpatterns = [
    path('login/', AccountLogin.as_view()),
    path('register/', AccountRegister.as_view()),
    path('accounts/', AccountList.as_view()),
    path('accounts/<int:pk>/', AccountDetail.as_view())
]