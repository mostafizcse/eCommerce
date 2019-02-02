
from django.urls import path
from . import views

app_name= 'blogApp'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog')
]
