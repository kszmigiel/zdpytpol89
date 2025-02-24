from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('costam/<str:arg>/', views.with_argument, name='with_argument'),
    path('costam/', views.with_query_param, name='with_query_param'),
    ]