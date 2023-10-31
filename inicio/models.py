from django.db import models

class Remera(models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.TextField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f'id : {self.id} - marca : {self.marca} - descripcion : {self.descripcion} - stock : {self.stock}'
    
class Zapatilla(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    stock = models.IntegerField()
    
    def __str__(self):
        return f'id : {self.id} - marca : {self.marca} - modelo : {self.modelo} - color : {self.color} - stock : {self.stock}'
    
class Gorra(models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.TextField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f'id : {self.id} - marca : {self.marca} - descripcion : {self.descripcion} - stock : {self.stock}'