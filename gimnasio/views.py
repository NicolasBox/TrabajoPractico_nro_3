from django.shortcuts import render, redirect
from .models import Socio, Entrenador, Clase
from .forms import SocioForm, EntrenadorForm, ClaseForm, SearchForm


def index(request):
    clases = Clase.objects.all()
    search_form = SearchForm()
    return render(request, 'gimnasio/index.html', {
        'clases': clases,
        'search_form': search_form
    })


def create_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = SocioForm()
    return render(request, 'gimnasio/socio_form.html', {'form': form})


def create_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntrenadorForm()
    return render(request, 'gimnasio/entrenador_form.html', {'form': form})


def create_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClaseForm()
    return render(request, 'gimnasio/clase_form.html', {'form': form})


def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            results = Socio.objects.filter(nombre__icontains=q)

    return render(request, 'gimnasio/search_results.html', {
        "results": results,
        'query': request.GET.get('q', '')
    })
