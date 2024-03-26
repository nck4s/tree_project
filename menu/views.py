from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    parent_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'menu.html', {'parent_items': parent_items})
