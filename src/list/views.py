from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import ListForm
# Create your views here.


def list_create_view(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListForm()

    context = {
        'form': form
    }

    return render(request, "list/create.html", context)


def list_update_view(request, id=id):
    obj = get_object_or_404(List, id=id)
    form = ListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../admin/')
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
        return redirect('../../admin/')
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
