from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  # camada extra para a funcao
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView



class CarsListView(ListView): # ja sabe que é GET, pois é uma view de listagem
   model = Car
   template_name = 'cars.html'
   context_object_name = 'cars'

   def get_queryset(self):
      cars = super().get_queryset().order_by('model')
      search = self.request.GET.get('search')
      if search:
         cars = cars.filter(model__icontains=search)
      return cars


class CarDetailView(DetailView):
   model = Car
   template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreteView(CreateView):
   model = Car
   form_class = CarModelForm
   template_name = 'new_car.html'
   success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
   model = Car # modelo
   form_class = CarModelForm  # formulario
   template_name = 'car_update.html' # html retornado pro usuario

   def get_success_url(self):
      return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) # (url, id)

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
   model = Car
   template_name = 'car_delete.html'
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
