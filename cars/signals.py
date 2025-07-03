from django.db.models.signals import  post_delete, post_save, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

def car_inventory_update():
   cars_count = Car.objects.all().count()
   cars_value = Car.objects.aggregate(
      total_value = Sum('value')
   )['total_value']

   CarInventory.objects.create(
      cars_count=cars_count,
      cars_value=cars_value
   )

#apos save ou edicao no banco
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
   car_inventory_update()

#apos exclusao no banco
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
   car_inventory_update()

#antes do save no banco
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
   if not instance.bio:
      instance.bio = 'Bio gerada automaticamente!'


'''
signals(manipulacao de eventos), é habilitado dentro de apps.py
sender = model que esta enviando o evento
instance = instancia do objeto que sera salvo
'''
