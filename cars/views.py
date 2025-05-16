from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
      cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request,
        'cars.html',
        {'cars': cars}
      )


# __ = navegacao entre tabelas que tem relacao
# __contains = filtrar por parte do nome
# __icontains = filtrar por parte do nome, sem diferenciar maiusculas e minusculas
# order_by = ordenacao de A-Z ou 1-9
