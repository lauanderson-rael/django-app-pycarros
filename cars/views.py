from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView


# ja sabe que é GET, pois é uma view de listagem
class CarsListView(ListView):
   model = Car
   template_name = 'cars.html'
   context_object_name = 'cars'

   def get_queryset(self):
      cars = super().get_queryset().order_by('model')
      search = self.request.GET.get('search')
      if search:
         cars = cars.filter(model__icontains=search)
      return cars



class NewCarCreteView(CreateView):
   model = Car
   form_class = CarModelForm
   template_name = 'new_car.html'
   success_url = '/cars/'



# class NewCarView(View):
#    def get (self, request):
#       new_car_form = CarModelForm()
#       return render(request, 'new_car.html', {'new_car_form': new_car_form})
#    def post(self, request):
#       new_car_form = CarModelForm(request.POST, request.FILES)
#       if new_car_form.is_valid():
#          new_car_form.save()
#          return redirect('cars_list')


# def cars_view(request):
#     cars = Car.objects.all().order_by('model')
#     search = request.GET.get('search')

#     if search:
#       cars = Car.objects.filter(model__icontains=search).order_by('model')

#     return render(
#         request,
#         'cars.html',
#         {'cars': cars}
#       )


# __ = navegacao entre tabelas que tem relacao
# __contains = filtrar por parte do nome
# __icontains = filtrar por parte do nome, sem diferenciar maiusculas e minusculas
# order_by = ordenacao de A-Z ou 1-9
