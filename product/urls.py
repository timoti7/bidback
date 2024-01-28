# product/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProductViewSet, RealEstateViewSet, VehicleViewSet, 
                    RealEstateOfferView)

router = DefaultRouter()
router.register(r'urunler', ProductViewSet, basename='product')
router.register(r'emlak', RealEstateViewSet, basename='real-estate')
router.register(r'tasit', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('', include(router.urls)),
    path('emlak/<int:product_id>/teklifler/', RealEstateOfferView.as_view(), name='real_estate_offer'),
]

