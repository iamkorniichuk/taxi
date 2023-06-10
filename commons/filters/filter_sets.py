from django.db.models.fields import DateTimeField, TextField, CharField, PositiveSmallIntegerField
from django.forms.widgets import TextInput

from django_filters import FilterSet
from django_filters.widgets import RangeWidget
from django_filters.filters import DateTimeFromToRangeFilter, RangeFilter, CharFilter

from commons.models import MoneyField

from .filters import EmptyStringFilter
from .widgets import *


class BootstrapFilterSet(FilterSet):
    FILTER_DEFAULTS = {
        CharField: {
            'filter_class': CharFilter,
            'extra': lambda f: {
                'widget': TextInput,
                'lookup_expr': 'contains'
            },
        },
        TextField: {
            'filter_class': EmptyStringFilter,
            'extra': lambda f: {
                'widget': SelectBooleanWidget,
                'exclude': True
            },
        },
        PositiveSmallIntegerField: {
            'filter_class': RangeFilter,
            'extra': lambda f: {
                'widget': RangeWidget,
            },
        },
        MoneyField: {
            'filter_class': RangeFilter,
            'extra': lambda f: {
                'widget': RangeWidget,
            },
        },
        DateTimeField: {
            'filter_class': DateTimeFromToRangeFilter,
            'extra': lambda f: {
                'widget': RangeWidget(attrs={
                    'type': 'date'
                }),
            },
        }
    }
