from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SportsfesItem
# Create your views here.

def sportsfesView(request):
    all_sportsfes_items = SportsfesItem.objects.all()
    return render(request, 'sportsfes.html', {'all_items': all_sportsfes_items})

def addSportsfes(request):
    new_item = SportsfesItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/sportsfes/')

def deleteSportsfes(request, sportsfes_id):
    item_to_delete = SportsfesItem.objects.get(id=sportsfes_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/sportsfes/')