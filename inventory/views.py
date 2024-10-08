from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data['name'],
                quantity=data['quantity'],
                barcode=data['barcode']
            )
            return JsonResponse({"message": "Product added successfully", "product_id": product.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_product_details(request, barcode):
    try:
        product = Product.objects.get(barcode=barcode)
        product_data = {
            'name': product.name,
            'quantity': product.quantity,
            'barcode': product.barcode
        }
        return JsonResponse(product_data, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    

#get all products
def get_all_products(request):
    products = Product.objects.all()
    products_list = []
    
    for product in products:
        products_list.append({
            'name': product.name,
            'quantity': product.quantity,
            'barcode': product.barcode
        })
    
    return JsonResponse(products_list, safe=False, status=200)