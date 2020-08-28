from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import ListForm
import requests
# Create your views here.


def list_create_view(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListForm()
        return redirect('../all/')
    context = {
        'form': form
    }

    return render(request, "list/create.html", context)


def list_update_view(request, id=id):
    obj = get_object_or_404(List, id=id)
    form = ListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../all/')
    context = {
        'form': form
    }
    return render(request, "list/create.html", context)


def list_detail_view(request, id):
    obj = get_object_or_404(List, id=id)
    context = {
        'object': obj
    }

    return render(request, "list/detail.html", context)


def list_delete_view(request, id):
    obj = get_object_or_404(List, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../all/')
    context = {
        'object': obj
    }

    return render(request, "list/delete.html", context)


def list_list_view(request):
    queryset = List.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "list/list.html", context)


def completed_view(request):
    completado = List.objects.filter(done = True)
    context = {
        "object_list": completado
    }
    return render(request, "list/completed.html", context)


def incomplete_view(request):
    incompleto = List.objects.filter(done = False)
    context = {
        "object_list": incompleto
    }
    return render(request, "list/incomplete.html", context)


def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoibGF1YXJpYXM5OCIsImEiOiJja2VkZXpraWEwMWM2MnRwNzdzdGhtN3BrIn0.ZVxB6Eeeifgoemxy28fwkg'
    return render(request, 'list/default.html', {'mapbox_access_token': mapbox_access_token})


def todays_cat(request):
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=1&page=10&order=Desc')
    data = response.json()
    print(data[0]["url"])
    return render(request, 'list/cat.html', {'url': data[0]['url']})
