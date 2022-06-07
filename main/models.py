from django.db import models
from ckeditor.fields import RichTextField



class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="banner_image", blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="category_image", blank=True, null=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title





class Company(models.Model):
    STATUS = [
        ('VIP', 'VIP'),
        ('NEW', 'NEW'),
        ('INACTIVE', 'INACTIVE'),
    ]

    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logos/")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.SET_NULL, null=True, blank=True)
    mobile = models.CharField(max_length=32, null=True, blank=True)
    instagram = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    website = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS, default="NEW")
    new = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    about = models.TextField()
    like_count = models.IntegerField(default=1)
    seen_count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    image = models.ImageField(
        upload_to="companies_posts_image/", null=True, blank=True)
    title = RichTextField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts_company")

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="product_company")

    def __str__(self):
        return self.title




class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="companies/")
    image_mobile = models.ImageField(
        upload_to="companies_mobile/", default="default.webp")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name="company_images")

    def __str__(self):
        return str(self.title)


class Counter(models.Model):
    visited_counter = models.IntegerField()

    def __str__(self):
        return str(self.visited_counter)


class ContactUs(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email")
    message = models.TextField(verbose_name="SMS")

    class Meta:
        verbose_name = 'Gelen Hat'
        verbose_name_plural = 'Gelen hatlar'

    def __str__(self):
        return self.email
