
from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('info/', views.info, name="info"),
    path('tableinfo/', views.tableinfo, name='tableinfo'),
    path('client/', views.clientform, name='form'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),

]
