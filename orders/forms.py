from commons.forms import BootstrapForm
from orders.models import Order
from django.contrib.gis import forms


class MapWidget(forms.OSMWidget):
    def __init__(self):
        super().__init__(attrs={
            'map_height': 500
        })


class CreateOrderForm(forms.ModelForm, BootstrapForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer', )

    _stops = forms.MultiPointField(widget=MapWidget())
