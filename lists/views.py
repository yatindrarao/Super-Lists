from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm, EMPTY_ITEM_ERROR

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id= list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            list_.delete()
            return render(request, 'lists.html', {"error": EMPTY_ITEM_ERROR})
    return render(request, 'lists.html', {'list': list_, 'error': EMPTY_ITEM_ERROR})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        return render(request, 'home.html', {"error": EMPTY_ITEM_ERROR})
    return redirect(list_)
