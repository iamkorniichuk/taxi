from django.core.validators import EMPTY_VALUES
from django.db.models import ForeignKey, Q
from django.db.models.fields import DateTimeField, TextField
from django.forms import RadioSelect, TextInput

from django_filters import FilterSet
from django_filters.widgets import RangeWidget, BooleanWidget
from django_filters.filters import DateTimeFromToRangeFilter, RangeFilter, BooleanFilter, CharFilter

from .models import MoneyField


class EmptyStringFilter(BooleanFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.field_name: ""})


class BootstrapBooleanWidget(RadioSelect):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = (("true", "Yes"), ("false", "No"), ('', 'Any'))


class BootstrapFilterSet(FilterSet):
    def find_by_full_name(self, queryset, name, value):
        first_name_lookup = '__'.join([name, 'first_name', 'contains'])
        last_name_lookup = '__'.join([name, 'last_name', 'contains'])
        return queryset.filter(
            Q(**{first_name_lookup: value}) | Q(**{last_name_lookup: value})
        )

    class Meta:
        filter_overrides = {
            ForeignKey: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'widget': TextInput,
                    'method': 'find_by_full_name'
                }
            },
            TextField: {
                'filter_class': EmptyStringFilter,
                'extra': lambda f: {
                    'widget': BooleanWidget,
                    'exclude': True
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
