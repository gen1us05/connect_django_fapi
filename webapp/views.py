from django.shortcuts import render
from django.views import View
from .models import Order, Product



class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        contex = {'products': products}
        return render(request, 'products.html', contex)






