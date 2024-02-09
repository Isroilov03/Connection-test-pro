from django.urls import path
from home.views import *

urlpatterns = [
    # --------------------- start CRUD urls Order_single model -----------------------------
    path('get-all-order-single-items/', get_all_single_order),
    path('create-order-single-item/<int:pk>/', create_order_single),
    path('update-order-single-item/<int:pk>/', update_order_single),
    path('delete-order-single-item/<int:pk>/', delete_order_single_model),
    # <<<<<<<<<<<<<<<<<<<<<< end CRUD urls Order_single model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    # <<<<<<<<<<<<<<<<<<<<<< start CRUD urls Product model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # path('get-all-order-single-items/', get_all_single_order),
    path('create-product-item/', create_product),
    path('update-product-item/<int:pk>/', update_product),
    # path('delete-order-single-item/<int:pk>/', delete_order_single_model),

]