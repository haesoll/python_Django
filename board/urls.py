from django.urls import path
from .views import index_hello

urlpatterns = [
    path('', index_hello, name='index_hello'),
]