from django.forms import ModelForm

from commons.forms import BootstrapForm

from .models import Order


class CreateOrderForm(ModelForm, BootstrapForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ("customer",)
