from django.urls import path

from . import views

urlpatterns = [
    path('category-list/', views.CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/', views.CategoryView.as_view(), name="category"),
    path('banner-list/', views.BannerListView.as_view(), name="banner-list"),
    path('post/', views.ContactFormListView.as_view(), name="post"),
    
    path('location-list/', views.LocationListView.as_view(), name="location-list"),
    path('company-list/', views.CompanyListView.as_view(), name="company-list"),
    path('company/<int:pk>/', views.CompanyView.as_view(), name="company"),
    path('company-vip-list/', views.VipListView.as_view(), name="company-vip-list"),
    path('counter/', views.CounterView.as_view(), name='counter'),
    path('company-visited/<int:pk>/',
         views.CompanyVisitedView.as_view(), name="company-visited"),
    path('company-liked/<int:pk>/',
         views.CompanyLikedView.as_view(), name="company-liked"),
]
