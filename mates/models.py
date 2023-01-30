from django.db import models

# Create your models here.
class Mate(models.Model):
    name = models.CharField(max_length=100, default="Mate")
    tipo = models.ForeignKey("Tipo", on_delete=models.CASCADE)
    color = models.ForeignKey("Color", on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="mates", blank=True, null=True) 
    alto = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True, null=True)
    ancho = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True, null=True)
    largo = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True, null=True)
    peso = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True, null=True)
    stock = models.IntegerField(default=0)
    sku = models.CharField(max_length=100, default="SKU 0000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " " + self.tipo.name + " " + self.color.name + " " + self.sku

class Tipo(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PriceHistory(models.Model):
    mate = models.ForeignKey("Mate", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mate + " " + str(self.price)
