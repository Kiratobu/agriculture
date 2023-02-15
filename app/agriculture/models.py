from django.db import models


class Farmer(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя')

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
    
class Plot(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название поля')
    # location = models.PointField()
    farmer = models.ForeignKey(Farmer,
                               on_delete=models.CASCADE,
                               related_name='farmer')
    culture = models.ForeignKey(Culture,
                                on_delete=models.CASCADE,
                                related_name='culture')
    season = models.ForeignKey(Season,
                               on_delete=models.CASCADE,
                               related_name='season')

    def __str__(self):
        return self.name