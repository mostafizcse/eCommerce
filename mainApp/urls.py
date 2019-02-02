"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

app_name = 'mainApp'

from . import views
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('product/<int:id>', views.ProductDetails.as_view(), name='product'),
    # path('hotdeal', views.HotDeal.as_view(), name='hotdeal'),
    # path('product/<slug>', views.ProductSlugView.as_view(), name='product_Slug'),
]