from django.db import models

# Create your models here.

class Farmer(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name
    
class Plot(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название поля')

    def __str__(self):
        return self.name
    
class Culture(models.Model):
    
    name = models.CharField(max_length=255,verbose_name='Название культуры')
    
    def __str__(self):
        return self.name
    
class Season(models.Model):
    
    name = models.CharField(max_length=255,verbose_name='Название сезона')
    
    def __str__(self):
        return self.name