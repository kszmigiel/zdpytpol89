from django.urls import path
from .views import index, login, image_view

urlpatterns = [
    path('', index, name='index'),
    path('images/', image_view, name='image'),
    path('images/<int:id>/', image_view, name='image'),
    path('login/', login, name='login'),
]
