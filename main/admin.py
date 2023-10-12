# from django.contrib import admin
# from main.forms import Product
# # Register your models here.
# admin.site.register(Product)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from .models import Product
from main.forms import Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0  # This determines how many empty inline forms are displayed

class UserAdmin(DefaultUserAdmin):
    inlines = [ProductInline]

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)
admin.site.register(Product)
