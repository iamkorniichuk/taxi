from orders.models import Order
from django.contrib.gis import forms


class MapWidget(forms.OSMWidget):
    def __init__(self):
        super().__init__(attrs={
            'map_height': 500
        })


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer', )

    start_point = forms.PointField(widget=MapWidget())
    end_point = forms.PointField(widget=MapWidget())
