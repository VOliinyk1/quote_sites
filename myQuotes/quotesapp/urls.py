from django.contrib import admin
from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [path('', views.main, name='root'),
               path('load_data_db', views.load_data, name='load_data'),
               path('author/<int:auth_id>', views.show_author, name='show_author'),
               path('author/add/', views.add_author, name='add_author'),
               path('quote/add/', views.add_quote, name='add_quote')]