from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
import json
import datetime
from django.db.models import Avg
#from passporteye import read_mrz
# Create your models here.


ORDER_STATUS = (
	(1, "In review"),
	(2, "Accepted"),
	(3, "Rejected")
)

class CustomUser(AbstractUser):
	user_phone = models.CharField(blank=True, max_length=35)
	user_address = models.CharField(blank=True, max_length=120)
	iin = models.CharField(blank=True, max_length=30)
	gender = models.CharField(blank=True, max_length=10)
	birthday = models.CharField(null=True, max_length=30) 
	uploadImage = models.ImageField('Аватар', upload_to = 'project-vue/src/assets/uploads')

class Customer(models.Model):
	user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, unique=True)
	user_name = models.CharField('Ник пользователя', max_length=35)
	customer_cardnumber = models.CharField('Номер карты', max_length=35)

class Baker(models.Model):
	user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, unique=True)
	baker_rating = models.FloatField('Рейтинг пекарей', default=0.0)

class ProductForm(models.Model):
	form_name = models.CharField('Имя формы', max_length=35)
	form_type = models.CharField('Тип формы', max_length=35)
	form_calory = models.IntegerField('Калории формы', default=0)
	form_description = models.TextField('Описание формы', max_length=120)

class ProductStuff(models.Model):
	stuff_name = models.CharField('Начинка', max_length=35)
	stuff_type = models.CharField('Тип Начинки', max_length=35)
	stuff_calory = models.IntegerField('Калории Начинки', default=0)
	stuff_description = models.TextField('Описание Начинки', max_length=120)

class ProductTopping(models.Model):
	topping_name = models.CharField('Посыпка', max_length=35)
	topping_type = models.CharField('Тип Посыпки', max_length=35)
	topping_calory = models.IntegerField('Калории Посырки', default=0)
	topping_description = models.TextField('Описание Посыпки', max_length=120)

class Order(models.Model):
	user = models.ForeignKey(CustomUser, related_name='customer_order', on_delete = models.CASCADE)
	baker = models.ForeignKey(CustomUser, related_name='baker_order', on_delete=models.CASCADE)
	order_total = models.IntegerField('Сумма заказа', default=0)
	order_address = models.CharField('Адрес заказа', max_length=120)
	order_date = models.DateField('Дата заказа')
	order_confirm = models.BooleanField(default=False)
	order_detail_text = models.TextField('Текст заказа', max_length=120)
	status = models.IntegerField(verbose_name="Статус", choices=ORDER_STATUS, default=1)

class Catalog(models.Model):
	catalog_name = models.CharField('Имя продукта', max_length=35)
	catalog_description = models.TextField('Описание Продукта', max_length=350)
	catalog_price = models.IntegerField('Цена продукта', default=0)
	catalog_rating = models.FloatField('Рейтинг продукта', default=0.0)
	catalog_calory = models.IntegerField('Калории продукта', default=0)
	catalog_image = models.ImageField('Картинка каталога', upload_to = 'project-vue/src/assets/catalog')
	catalog_date = models.DateField()
	catalog_expiredate = models.DateField()
	catalog_type = models.CharField('Тип продукта', max_length=35)
	baker = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
	# form = models.ForeignKey(ProductForm, on_delete = models.CASCADE)
	catalog_form = models.ForeignKey(ProductForm, on_delete = models.CASCADE, null=True, blank=True)
	catalog_stuff = models.ForeignKey(ProductStuff, on_delete = models.CASCADE, null=True, blank=True)
	catalog_topping = models.ForeignKey(ProductTopping, on_delete = models.CASCADE, null=True, blank=True)
	# tags = TaggableManager()

class Product(models.Model):
	product_name = models.CharField('Имя', max_length=35)
	manufacture_date = models.DateField('Дата производства')
	expire_date = models.DateField('Срок годности')
	product_type = models.CharField('Тип продукта', max_length=35)
	customized = models.BooleanField(default=True)
	#product_form = models.CharField('Форма продукта', max_length=35, null=True)
	productform = models.ForeignKey(ProductForm, on_delete = models.CASCADE, null=True, blank=True)
	productstuff = models.ForeignKey(ProductStuff, on_delete = models.CASCADE, null=True, blank=True)
	producttopping = models.ForeignKey(ProductTopping, on_delete = models.CASCADE, null=True, blank=True)
	product_detailtext = models.CharField('Надпись', max_length=350)
	product_calory = models.IntegerField('Калории Продукта', default=0)
	order = models.ForeignKey(Order, on_delete = models.CASCADE)
	product_cost = models.IntegerField('Стоимость продукта', default=0)
	product_catalog_id = models.ForeignKey(Catalog,blank=True, null=True, on_delete=models.SET_NULL)

class Review(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

# class BakerModel(models.Model):
#  	id = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True, blank=True)
#  	iin = models.CharField("IIN")

class ImageModel(models.Model):
	imageUpload = models.ImageField('Удостоверение', upload_to = 'project-vue/src/assets/passport')
	name = models.CharField('Имя', max_length=35, null=True, blank=True)
	surname = models.CharField('Фамилия', max_length=35, null=True, blank=True)
	iin = models.CharField(blank=True, max_length=30)
	gender = models.CharField(blank=True, max_length=10)
	birthday = models.CharField(null=True, max_length=30) 

	# def __str__(self):
	#     mrz = read_mrz(self.imageUpload.read(), save_roi=True)
	#     mrz_data = mrz.to_dict()
	#     return Response(mrz_data)

