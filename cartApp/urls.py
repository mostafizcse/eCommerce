from django.urls import path
from . import views
app_name = 'cartApp'
urlpatterns = [
    path('', views.CartView.as_view(), name='cart_list')
]