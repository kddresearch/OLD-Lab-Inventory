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
]

urlpatterns += normalpatterns