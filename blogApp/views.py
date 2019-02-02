from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class BlogHome(TemplateView):
    template_name = 'blogapp/blog.html'
