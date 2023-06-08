from django.db.models import ForeignKey, Q
from django.forms import TextInput
from django_filters.filters import CharFilter

from django_filters.filters import MultipleChoiceFilter, OrderingFilter, BooleanFilter
from django.forms.widgets import CheckboxSelectMultiple

from commons.filters.filter_sets import BootstrapFilterSet
from commons.filters.widgets import SelectBooleanWidget
from cars.models import TypeChoices, ClassChoices

from .models import Order


class OrderFilterSet(BootstrapFilterSet):
    class Meta:
        model = Order
        fields = '__all__'

    ordering = OrderingFilter(
        fields=[
            ('datetime', 'datetime'),
            ('price', 'price'),
        ],
        empty_label=None,
        null_label=None
    )

    customer = CharFilter(field_name='customer',
                          method='find_by_full_name', widget=TextInput)
    is_open = BooleanFilter(field_name='is_open', label='Is open',
                            widget=SelectBooleanWidget)
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

    def find_by_full_name(self, queryset, name, value):
        first_name_lookup = '__'.join([name, 'first_name', 'contains'])
        last_name_lookup = '__'.join([name, 'last_name', 'contains'])
        return queryset.filter(
            Q(**{first_name_lookup: value}) | Q(**{last_name_lookup: value})
        )
