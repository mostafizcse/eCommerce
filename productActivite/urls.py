
from django.urls import path

from . import views

app_name = 'productActivite'
urlpatterns = [
    # path('add', views.AddComporisoon.as_view(), name='add'),
    path('', views.ComporisoonProduct.as_view(), name='comporisoon'),
    path('delete/<int:id>', views.delete_comporision, name='delete')
]