
from django.urls import path
from .views import (
    products_view,
    products_detail_view, 
    products_create_view,
    products_delete_view,
    products_delete_success
)
app_name='products'
urlpatterns = [
    path('', products_view),
    path('<int:my_id>/detail', products_detail_view, name="products_detail"),
    path('create', products_create_view),
    path('<int:my_id>/delete', products_delete_view, name="products_delete"),
    path('<int:my_id>/delete_success', products_delete_success),
]