from django.forms import CheckboxSelectMultiple
from django_filters.filters import MultipleChoiceFilter, OrderingFilter, BooleanFilter

from commons.filters import BootstrapFilterSet, BootstrapBooleanWidget
from cars.models import TypeChoices, ClassChoices

from .models import Order


class OrderFilterSet(BootstrapFilterSet):
    class Meta(BootstrapFilterSet.Meta):
        model = Order
        fields = '__all__'
        exclude = ('_stops', )

    ordering = OrderingFilter(
        fields=[
            ('price', 'price'),
            ('datetime', 'datetime'),
        ],
        empty_label=None,
        null_label=None
    )

    is_open = BooleanFilter(field_name='is_open', label='Is open',
                            widget=BootstrapBooleanWidget)
    car_type = MultipleChoiceFilter(choices=TypeChoices.choices,
                                    widget=CheckboxSelectMultiple)
    car_class = MultipleChoiceFilter(choices=ClassChoices.choices,
                                     widget=CheckboxSelectMultiple)

    @property
    def qs(self):
        queryset = super().qs
        user = self.request.user
        if not user.has_perm('orders.view_order'):
            queryset = queryset.filter(customer=user)
        if not user.has_perm('trips.view_trip'):
            queryset = queryset.filter(is_open=True)
        return queryset

    
