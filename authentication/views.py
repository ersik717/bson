from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from authentication.models import CustomUser, Customer, Product, ProductForm, ProductStuff, ProductTopping, Baker, Order, Catalog, Review, ImageModel #, BakerModel
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic.base import View
from .serializers import (
MyTokenObtainPairSerializer, 
CustomUserSerializer, 
UserListSerializer, 
ProductListSerializer, 
ProductDetailSerializer, 
ProductFormListSerializer, 
ProductFormDetailSerializer,
ProductStuffListSerializer, 
ProductStuffDetailSerializer, 
ProductToppingListSerializer, 
ProductToppingDetailSerializer, 
CustomerListSerializer, 
CustomerDetailSerializer, 
OrderListSerializer, 
OrderDetailSerializer, 
CatalogListSerializer, 
CatalogDetailSerializer, 
ReviewListSerializer, 
ReviewDetailSerializer, 
ImageModelSerializer, 
BakerCreateSerializer, 
BakerListSerializer,
CatalogCreateSerializer,
OrderCreateSerializer )
#, BakerDetailSerializer  
from .permission import IsOwnerOrReadOnly, IsSameUserAllowEditionOrReadOnly
from django.db.models import Count
from django.views.generic import TemplateView
from django.conf.urls import url,include
from django.contrib import admin   
from PIL import Image
from django.core.files import File
import PIL.Image as Image
import io 
from django.db import models

# Create your views here.
class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    queryset = CustomUser.objects.all()


class CustomUserCreate(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request, format='json'):
		serializer = CustomUserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				json = serializer.data
				return Response(json, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginPage(View):
	def get(self, request):
		return render(request, "frontend/login.html")

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    permission_classes = (permissions.AllowAny,)

class UserDetailView(generics.RetrieveAPIView):
	serializer_class = UserListSerializer
	queryset = CustomUser.objects.all()
	permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

class BakerCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BakerCreateSerializer
    queryset = CustomUser.objects.all()
    # def post(self, request, format='json'):
    #     serializer = BakerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             json = serializer.data
    #             return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BakerListView(generics.ListAPIView):
    serializer_class = BakerListSerializer
    queryset = Baker.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    permission_classes = (permissions.AllowAny,)

class BakerDetailView(generics.RetrieveAPIView):
    serializer_class = BakerListSerializer
    queryset = Baker.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()
    #permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerDetailSerializer
    queryset = Customer.objects.all()
    #permission_classes = (IsAuthenticated)

class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerDetailSerializer

# class BakerListView(generics.ListAPIView):
#     serializer_class = BakerListSerializer
#     queryset = Baker.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

# class BakerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BakerDetailSerializer
#     queryset = Baker.objects.all()
#     #permission_classes = (IsAuthenticated)

# class BakerCreateView(generics.CreateAPIView):
#     serializer_class = BakerDetailSerializer

class ProductListView(generics.ListAPIView):
	serializer_class = ProductListSerializer
	queryset = Product.objects.all()
	permission_classes = (IsOwnerOrReadOnly,)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    #permission_classes = (IsAuthenticated)
    permission_classes = (AllowAny,)

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (permissions.AllowAny,)

class ProductFormListView(generics.ListAPIView):
	serializer_class = ProductFormListSerializer
	queryset = ProductForm.objects.all()
	permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

class ProductFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductFormDetailSerializer
    queryset = ProductForm.objects.all()
    #permission_classes = (IsAuthenticated)

class ProductFormCreateView(generics.CreateAPIView):
    serializer_class = ProductFormDetailSerializer

class ProductStuffListView(generics.ListAPIView):
    serializer_class = ProductStuffListSerializer
    queryset = ProductStuff.objects.all()
    permission_classes = (permissions.AllowAny,)
	

class ProductStuffDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductStuffDetailSerializer
    queryset = ProductStuff.objects.all()
    #permission_classes = (IsAuthenticated)

class ProductStuffCreateView(generics.CreateAPIView):
    serializer_class = ProductStuffDetailSerializer

class ProductToppingListView(generics.ListAPIView):
	serializer_class = ProductToppingListSerializer
	queryset = ProductTopping.objects.all()
	permission_classes = (permissions.AllowAny,)

class ProductToppingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductToppingDetailSerializer
    queryset = ProductTopping.objects.all()
    #permission_classes = (IsAuthenticated)

class ProductToppingCreateView(generics.CreateAPIView):
    serializer_class = ProductToppingDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(baker=user)

class OrderUserListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

class OrderProductsView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        order_id = self.kwargs.get('pk')
        return Product.objects.filter(order=order_id)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CatalogListView(generics.ListAPIView):
    serializer_class = CatalogListSerializer
    queryset = Catalog.objects.all()
    permission_classes = (permissions.AllowAny,)

class BakerCatalogListView(generics.ListAPIView):
    serializer_class = CatalogListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return Catalog.objects.filter(baker=user)


class CatalogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatalogDetailSerializer
    queryset = Catalog.objects.all()
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (IsAuthenticated)

class CatalogCreateView(generics.CreateAPIView):
    serializer_class = CatalogCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()
    permission_classes = (permissions.AllowAny,)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
    permission_classes = (permissions.AllowAny,)
    #permission_classes = (IsAuthenticated)

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = (permissions.AllowAny,)

class ImageModelListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ImageModelSerializer
    queryset = ImageModel.objects.all()

    def post(self, request, format='json'):
        serializer = ImageModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ImageModelCreateView(generics.CreateAPIView):
    serializer_class = ImageModelSerializer
    queryset = ImageModel.objects.all()
    permission_classes = (permissions.AllowAny,)
   


class ClubChartView(TemplateView):
    template_name = 'project-vue/body.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = CustomUser.objects.all()
        return context


class Test(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        from passporteye import read_mrz
        mrz = read_mrz('http://127.0.0.1:8000/media/project-vue/src/assets/passport/' + 'sa_JU7r2P5.jpg')
        mrz_data = mrz.to_dict()
        return Response(mrz_data)