from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from main.models import ContactUs

from main.models import Category, Location, Company, Image, Counter, Banner, Post, Menu, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'title', 'image')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = fields = ('id', 'title', 'image')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ImageSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image', 'image_mobile')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    company_images = ImageSerailizer(read_only=True, many=True)
    category = CategorySerializer()
    location = LocationSerializer()
    menu = MenuSerializer()
    product_company = ProductSerializer(read_only=True, many=True)
    posts_company = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = "__all__"

class VipCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'logo')


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"


class CompanyVisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
