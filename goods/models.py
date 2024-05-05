from pyclbr import Class
from tabnanny import verbose
from django.conf.global_settings import DEFAULT_FILE_STORAGE
from django.db import models

class Categories(models.Model):
    name=models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table='category'
        verbose_name='категорию'
        verbose_name_plural='категории'
        
    def __str__(self):
            return self.name
        
    

    

class Products(models.Model):
    name=models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description=models.TextField(blank=True, null=True, verbose_name='Описание')
    image=models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    insdepth=models.CharField(default=0, max_length=150, verbose_name='Глубина профиля')
    numofchamb=models.DecimalField(default=0, max_digits=2, decimal_places=0, verbose_name='Количество камер')
    epdmgaskets=models.DecimalField(default=0, max_digits=2, decimal_places=0, verbose_name='Количество уплотнителей')
    soundinstall=models.CharField(default=0, max_length=150, verbose_name='Коэффициент звукоизоляции')
    thermaltransm=models.CharField(default=0, max_length=25, verbose_name='Коэффициент теплоотдачи')
    category=models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    
    class Meta:
        db_table='product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        
    def __str__(self):
            return f'{self.name} Количество камер - {self.numofchamb}'

    
    def display_id(self):
        return f'{self.id:05}'