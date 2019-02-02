
from django.urls import path

from . import views

app_name= 'customarApp'

urlpatterns = [
    path('registration', views.CustomarRegistration.as_view(), name='registration'),
]
