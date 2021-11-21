from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from service.models import *
import json


# Create your views here.

def service_index(request):
    data = {}
    return render(request, 'service detail.html', data)

class ProductList(View):
    def get(self, request):
        products = list(Product.objects.all().values())
        data = dict()
        data['products'] = products
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        data = dict()
        data['products'] = model_to_dict(product)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class ProductListt(View):
    def get(self, request):

        product = Product.objects.order_by(
            'prod_id').values('prod_id','prod_name','prod_price','prod_img')

#         # newProduct = []
#         # index = 0

#         # for p in product:
#         #     product = Product.objects.values().get(
#         #         prod_id=p['prod_id'])
#         #     p['product_name'] = product['prod_name']
#         #     p['product_price'] = float(product['prod_price'])
#         #     p['product_img'] = product['prod_img']

#         #     if (index == 0):
#         #         newProduct.append(p)
#         #         newProduct[-1]['count'] = 1
#         #     else:
#         #         if (product[index-1]['product_id'] != p['product_id']):
#         #             newProduct.append(p)
#         #             newProduct[-1]['count'] = 1
#         #         else:
#         #             newProduct[-1]['count'] += 1

#         #     index += 1

#         # product_json = json.dumps(product)

        return HttpResponse(product, content_type='application/json')
