from django.contrib import admin
from .models import CustomUser, Product, ProductForm, ProductStuff, ProductTopping, Customer, Baker, Order, Catalog, Review, ImageModel #, BakerModel
#from .views import Test
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
	model = CustomUser

class ProductAdmin(admin.ModelAdmin):
	model = Product

class ProductFormAdmin(admin.ModelAdmin):
	model = Product

class ProductStuffAdmin(admin.ModelAdmin):
	model = Product

class ProductToppingAdmin(admin.ModelAdmin):
	model = Product

class CustomerAdmin(admin.ModelAdmin):
	model = Customer

class BakerAdmin(admin.ModelAdmin):
	model = Baker

class OrderAdmin(admin.ModelAdmin):
	model = Order

class CatalogAdmin(admin.ModelAdmin):
	model = Catalog

class ReviewAdmin(admin.ModelAdmin):
	model = Review

class ImageModelAdmin(admin.ModelAdmin):
	model = ImageModel

# class BakerModelAdmin(admin.ModelAdmin):
# 	model = Baker

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductForm, ProductFormAdmin)
admin.site.register(ProductStuff, ProductStuffAdmin)
admin.site.register(ProductTopping, ProductToppingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Baker, BakerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Catalog, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ImageModel, ImageModelAdmin)
#admin.site.register(Baker, BakerModelAdmin)