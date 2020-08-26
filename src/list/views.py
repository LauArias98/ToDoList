from django.shortcuts import render
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


def list_detail_view(request):
    obj = List.objects.get(id=1)
    context = {
        'object': obj
    }

    return render(request, "list/detail.html", context)