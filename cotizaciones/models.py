import datetime
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

class Cotizacion(models.Model):
    cliente = models.CharField(max_length=200)
    fecha = models.DateField(default=timezone.now)
    distrito = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, blank=True, null=True)
    adicional = models.TextField(max_length=500)
    #guarda la fecha y hora creada de la cotizacion (backend)
    fecha_hora = models.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            val_cot = ValorCotizacion.objects.get(cotizacion=self)
        except ValorCotizacion.DoesNotExist:
            obj_val_cot = ValorCotizacion(cotizacion=self, valor_subtotal=0.00, valor_igv=0.00, valor_total=0.00)
            # super().save(*args, **kwargs)
            obj_val_cot.save()
    def __str__(self):
        return self.cliente

class ItemCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)
    cantidad = models.PositiveIntegerField(default=1)
    opc_unidad = (
        ('m2', 'metro cuadrado'),
    )
    unidad = models.CharField(max_length=20, choices=opc_unidad, default="m2")
    val_unit = models.DecimalField(default=0.01, max_digits=17, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    total_item = models.DecimalField(default=0.01, max_digits=17, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    def save(self, *args, **kwargs):    
        if not self.pk:
            tot_item = self.val_unit * Decimal(self.cantidad)
            self.total_item = Decimal(round(tot_item, 2))
            obj_val_cot = ValorCotizacion.objects.get(cotizacion=self.cotizacion)
            obj_val_cot.valor_subtotal += self.total_item
            imp = obj_val_cot.valor_subtotal * Decimal(0.18)
            total = obj_val_cot.valor_subtotal + imp
            imp_red = round(imp, 2)
            total_red = round(total, 2)
            obj_val_cot.valor_igv = imp_red
            obj_val_cot.valor_total = total_red
            obj_val_cot.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.descripcion

class ValorCotizacion(models.Model):
    cotizacion = models.OneToOneField(Cotizacion, on_delete=models.CASCADE, primary_key=True)
    valor_subtotal = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    valor_igv = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    valor_total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    def __str__(self):
        return self.cotizacion.cliente


@receiver(post_delete, sender=ItemCotizacion)
def item_delete(sender, instance, **kwargs):
    cot = ValorCotizacion.objects.get(cotizacion=instance.cotizacion)
    cot.valor_subtotal -= instance.total_item
    cot.valor_igv = cot.valor_subtotal * Decimal(0.18)
    cot.valor_total = cot.valor_subtotal + cot.valor_igv
    cot.save()



