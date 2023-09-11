from django.shortcuts import render
from datetime import date

# Create your views here.
def show_main(request):
    context = {
        'name' : "Aqua",
        'amount' : 12,
        'description': 'PT. Danone',
        'date_in': date.today(),
        'stock': True,
        'categories': 'Beverages',
    }
    return render(request, "main.html", context)
