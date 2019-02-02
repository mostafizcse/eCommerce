from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Tag)

class SubCatInCategory(admin.TabularInline):
    model = SubCategory
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        Model = Category
    inlines = [SubCatInCategory]
admin.site.register(Category, CategoryAdmin)

# ====================================================================== Sub Category
class SubCategoryAdmin(admin.ModelAdmin):
    class Meta:
        Model = SubCategory
admin.site.register(SubCategory, SubCategoryAdmin)

# =========================================================================== Products

class ProductImgInProduct(admin.TabularInline):
    model = ProductImages
    extra = 1
admin.site.register(ProductImages)

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        Model = Product
    inlines = [ProductImgInProduct]
admin.site.register(Product, ProductAdmin)


class BannerSliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'posted_on']
    class Meta:
        Model = BannerSlider
admin.site.register(BannerSlider, BannerSliderAdmin)

admin.site.register(HotDeal)
admin.site.register(TodayDeal)
admin.site.register(SpeacialDeal)
