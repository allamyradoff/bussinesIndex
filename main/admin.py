from tkinter import Menu
from django.contrib import admin

from .models import Category, ContactUs, Location, Company, Image, Counter, Banner, Post, Menu, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]


class IndividualBirdAdmin(CategoryAdmin):
    image_fields = ['image', ]







admin.site.register(Category, IndividualBirdAdmin)
admin.site.register(Banner)
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Menu)
admin.site.register(ContactUs)
admin.site.register(Location)
admin.site.register(Company)
admin.site.register(Image)
admin.site.register(Counter)
