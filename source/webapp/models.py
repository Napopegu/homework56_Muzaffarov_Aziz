from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Наименование")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Наименование")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='products',
                                 verbose_name="Категория")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')
    image = models.URLField(verbose_name='Изображение')
    qty = models.PositiveIntegerField(default=1, verbose_name='Остаток')