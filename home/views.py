from django.shortcuts import render
from main.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import Order_singleSer, ProductSer

"""" start CRUD Order_Single model """
#read Order_single objects
@api_view(['GET'])
def get_all_single_order(request):
    orders = Order_single_product.objects.all().order_by('-id')
    ser = Order_singleSer(orders, many=True)
    return Response(ser.data)


#create Order_single object
@api_view(['POST'])
def create_order_single(request, pk):
    product_id = Product.objects.get(pk=pk)
    user_id = request.POST['user_id']
    branch_id = request.POST['branch_id']
    quantity = request.POST['quantity']
    is_delivery = request.POST['is_delivery']
    address = request.POST.get('address')
    delivery_date = request.POST.get('delivery_date')
    delivery_code = request.POST.get('delivery_code')
    is_active = request.POST.get('is_active')
    extra_phone_number = request.POST['extra_phone_number']
    total_price = product_id.cost * int(quantity)
    order = Order_single_product.objects.create(
    user_id=user_id,
    product_id=product_id,
    branch_id_id=branch_id,
    quantity=quantity,
    is_delivery=is_delivery,
    address=address,
    delivery_date=delivery_date,
    delivery_code=delivery_code,
    is_active=is_active,
    extra_phone_number=extra_phone_number,
    total_price=total_price,
    )
    ser = Order_singleSer(order)
    return Response(ser.data)


#edit Order_single object
@api_view(['PUT'])
def update_order_single(request, pk):
    order = Order_single_product.objects.get(pk=pk)
    product_id =request.POST['product_id']
    branch_id = request.POST['branch_id']
    quantity = request.POST['quantity']
    is_delivery = request.POST['is_delivery']
    address = request.POST.get('address')
    delivery_date = request.POST.get('delivery_date')
    delivery_code = request.POST.get('delivery_code')
    is_active = request.POST['is_active']
    extra_phone_number = request.POST['extra_phone_number']
    total_price = product_id.cost * quantity
    order.product_id = product_id
    order.product_id = branch_id
    order.quantity = quantity
    order.is_delivery = is_delivery
    order.address = address
    order.is_active = is_active
    order.extra_phone_number = extra_phone_number
    order.delivery_date = delivery_date
    order.delivery_code = delivery_code
    order.total_price = total_price
    ser = Order_singleSer(order)
    return Response(ser.data)



#delete Order_single object
@api_view(['DELETE'])
def delete_order_single_model(request, pk):
    order = Order_single_product.objects.get(pk=pk)
    order.delete()
    return Response({"message": "Deleted"})


"""" end CRUD Order_Single model """


"""" start CRUD Product model """

@api_view(['POST'])
def create_product(request):
    full_name = request.POST['full_name']
    brand_id = request.POST['brand']
    seller_id = request.POST['seller']
    subcategory_id = request.POST['subcategory']
    size_type_id = request.POST['size_type']
    tags = request.POST.getlist('tag')
    cost = request.POST['cost']
    images = request.FILES.getlist('images')
    quantity = request.POST['quantity']
    is_banner = request.POST.get('is_banner')
    is_sale = request.POST.get('is_sale')
    old_cost = request.POST.get('old_cost')
    sale_expire = request.POST.get('sale_expire')
    is_active = request.POST.get('is_active')
    rating = request.POST.get('rating')
    new_product = Product.objects.create(
        full_name=full_name,
        brand_id=brand_id,
        seller_id=seller_id,
        subcategory_id=subcategory_id,
        size_type_id=size_type_id,
        cost=cost,
        quantity=quantity,
        is_banner=is_banner,
        is_sale=is_sale,
        old_cost=old_cost,
        sale_expire=sale_expire,
        is_active=is_active,
        rating=rating,
    )
    for i in tags:
        new_product.tag.add(i)
        new_product.save()
    for i in images:
        img = Image.objects.create(image=i)
        new_product.images.add(img)
        new_product.save()
    ser = ProductSer(new_product)
    return Response(ser.data)



@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    full_name = request.POST['full_name']
    brand_id = request.POST['brand']
    seller_id = request.POST['seller']
    subcategory_id = request.POST['subcategory']
    size_type_id = request.POST['size_type']
    tags = request.POST.getlist('tag')
    cost = request.POST['cost']
    images = request.FILES.getlist('images')
    quantity = request.POST['quantity']
    is_banner = request.POST.get('is_banner')
    is_sale = request.POST.get('is_sale')
    old_cost = request.POST.get('old_cost')
    sale_expire = request.POST.get('sale_expire')
    is_active = request.POST.get('is_active')
    rating = request.POST.get('rating')
    product.full_name = full_name
    product.brand_id = brand_id
    product.seller_id = seller_id
    product.subcategory_id = subcategory_id
    product.size_type_id = size_type_id
    product.cost = cost
    product.quantity = quantity
    product.is_banner = is_banner
    product.is_sale = is_sale
    product.old_cost = old_cost
    product.sale_expire = sale_expire
    product.is_active = is_active
    product.rating = rating
    for i in tags:
        product.tag.add(i)
        product.save()
    for i in images:
        img = Image.objects.create(image=i)
        product.images.add(img)
        product.save()
    ser = ProductSer(product)
    return Response(ser.data)












