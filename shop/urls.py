from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, PaymentViewSet, ArrangementTypeViewSet, BuyerViewSet

router = DefaultRouter()
router.register(r'flowers', FlowerViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'arrangements', ArrangementTypeViewSet)
router.register(r'buyers', BuyerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]