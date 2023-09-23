from django.urls import path
from main.views import (
    show_main,
    create_product,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user,
    increase_quantity,  
    decrease_quantity,  
    delete_product,    
) 
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
]