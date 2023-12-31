from django.urls import path
from main.views import *
app_name = "main"
urlpatterns = [
    path('', show_main, name = 'show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase-quantity/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('delete-product-ajax/<int:product_id>/', delete_product_ajax, name='delete_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]