from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView


# Create your views here.

class BaseSite(View):
    template_name = 'base-site.html'
    def get(self, request):
        cat = SubCategory.objects.all()
        context= {
            'cat': cat
        }
        return render(request, self.template_name, context)

#  ======================================  components
# class HotDeal(View):
#     template_name = 'component/hot-deal.html'
#     def get(self, request):
#         # Hot Deal Section
#         hot_deal = HotDeal.objects.all()
#         context = {
#             'hot_deal': hot_deal,
#         }
#         return render(request, self.template_name, context)

class index(View):
    template_name = 'index.html'
    def get(self, request):
        bannerSlider = BannerSlider.objects.all()
        product = Product.objects.all()
        new_tag = get_object_or_404(Tag, name='new')
        new = Product.objects.filter(tag=new_tag)
        hot_tag = get_object_or_404(Tag, name='hot')
        hot = Product.objects.filter(tag=hot_tag)
        sale_tag = get_object_or_404(Tag, name='sale')
        sale = Product.objects.filter(tag=sale_tag)

        # Speacial Deal
        special_deal_1 = SpeacialDeal.objects.all().exclude()[:4]
        special_deal_2 = SpeacialDeal.objects.all().exclude()[4:8]
        special_deal_3 = SpeacialDeal.objects.all().exclude()[8:12]

        # Hot Deal Section
        hot_deal = HotDeal.objects.all()

        """ By Item Category """
        cat = Category.objects.all()

        context = {
            'banner': bannerSlider,
            'product': product,
            'new': new,
            'sale': sale,
            'hot': hot,
            'hot_deal': hot_deal,
            'special_deal_1': special_deal_1,
            'special_deal_2': special_deal_2,
            'special_deal_3': special_deal_3,
            'cat': cat
        }
        return render(request, self.template_name, context)

class ProductDetails(View):
    template_name = 'product-details.html'
    def get(self, request, id):
        post = get_object_or_404(Product, pk=id)
        today_deal = TodayDeal.objects.all().exclude()[:3]
        context = {
            'post': post,
            'today_deal': today_deal
        }
        return render(request, self.template_name, context)

# class ProductSlugView(DetailView):
#     model = Product
#     queryset = Product.objects.all()
#     def get_context_data(self,*args, **kwargs):
#         sq = super(ProductSlugView, self).get_context_data(*args, **kwargs)
#         return sq