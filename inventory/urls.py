from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
]

normalpatterns = [
    url(r'^login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name ='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='inventory/homepage.html'), name ='logout'),
    url(r'^register/', views.register,name ='register'),
    url(r'^home/', views.home, name='home'),
    url(r'^orders/', views.orders, name='orders'),
    url(r'^new_order/', views.new_order, name='new_order'),
    url(r'^item/', views.item, name='item'),
    url(r'^new_item/', views.new_item, name='new_item'),
    url(r'^vendor/', views.vendor, name='vendor'),
    url(r'^new_vendor/', views.new_vendor, name='new_vendor'),
    url(r'^location/', views.location, name='location'),
    url(r'^new_location/', views.new_location, name='new_location'),
    url(r'^category/', views.category, name='category'),
    url(r'^new_category/', views.new_category, name='new_category'),
]

urlpatterns += normalpatterns