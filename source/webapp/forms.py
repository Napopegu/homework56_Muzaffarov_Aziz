from django import forms
from webapp.models import Category, Product


class ProductForm(forms.Form):
    title = forms.CharField(max_length=50, label="Наименование")
    description = forms.CharField(max_length=200, label='Описание')
    price = forms.DecimalField(decimal_places=2, max_digits=7, label='Стоимость')
    image = forms.URLField(label='Изображение')
    qty = forms.IntegerField(label='Остаток', min_value=0)
    category = forms.ModelChoiceField(label="Категория", queryset=Category.objects.all())

    def clean_title(self):
        title = self.cleaned_data['title']
        title_old = self.initial.get('title')
        if not title_old or title != title_old:
            if Product.objects.filter(title=title).exists():
                raise forms.ValidationError('Продукт с таким названием существует')
        return title
