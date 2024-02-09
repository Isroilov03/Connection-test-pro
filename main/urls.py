from django.urls import path
from .views import *


urlpatterns = [
    path('filter-user-by-username/', filter_user_by_username),    #checked
    path('filter-product-by-price/', filter_product_by_price),
    path('filter-product-by-price-and-subcategory/<int:pk>/', filter_product_by_price_and_subcategory),
    path('filter-product-by-subcategory/', filter_product_by_subcategory),
    path('filter-product-by-rating/', filter_product_by_rating),
]