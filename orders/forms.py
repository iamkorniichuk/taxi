from commons.forms import BootstrapForm
from orders.models import Order
from django.contrib.gis import forms


class MapWidget(forms.OSMWidget):
    def __init__(self):
        super().__init__(attrs={
            'map_height': 500,
            'map_srid': 4326,
            'default_lat': 50.2547,
            'default_lon': 28.6587,
            'default_zoom': 12
        })


class CreateOrderForm(forms.ModelForm, BootstrapForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer', )

    _stops = forms.MultiPointField(widget=MapWidget())
