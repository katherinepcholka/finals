from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, help_text='Имя')
    last_name = forms.CharField(max_length=100, help_text='Фамилия')
    email = forms.EmailField(help_text='Email')
    phone = forms.CharField(max_length=20, help_text='Телефон')
    address = forms.CharField(max_length=200)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)


    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "phone", "postal_code", "city", "address")

    