# product/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
import json
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Product, RealEstate, Vehicle, Offer
from .serializers import ProductSerializer, RealEstateSerializer, VehicleSerializer, OfferSerializer


class CSRFTokenView(APIView):
    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)
        return Response({'csrfToken': csrf_token})

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RealEstateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class RealEstateOfferView(APIView):
    permission_classes = [IsAuthenticated]  # Kullanıcı yetkilendirme kontrolü

    def get(self, request, product_id):
        offers = Offer.objects.filter(product_id=product_id)
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product_id=product_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

