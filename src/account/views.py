from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def index_view(request):
    return render(request, 'login/index.html')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../admin')
    else:
        form = UserCreationForm()
        return render(request, 'login/register.html', {"form": form})

