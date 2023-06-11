from django.db.models import Q
from django.forms import TextInput
from django_filters.filters import CharFilter, BooleanFilter, OrderingFilter

from commons.filters.filter_sets import BootstrapFilterSet
from commons.filters.widgets import SelectBooleanWidget

from .models import Report


class ReportFilterSet(BootstrapFilterSet):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ('trip', 'report_datetime', 'complete_datetime', 'answer', 'message')

    ordering = OrderingFilter(
        fields=[
            ('report_datetime', 'report_datetime')
        ],
        empty_label=None,
        null_label=None
    )

    manager = CharFilter(field_name='manager',
                          method='find_by_full_name', widget=TextInput)
    is_completed = BooleanFilter(field_name='is_completed', label='Is completed',
                            widget=SelectBooleanWidget)

    @property
    def qs(self):
        queryset = super().qs
        user = self.request.user
        if not user.has_perm('reports.view_report'):
            queryset = queryset.filter(Q(manager=user) | Q(trip__order__customer=user))
        return queryset

    def find_by_full_name(self, queryset, name, value):
        first_name_lookup = '__'.join([name, 'first_name', 'contains'])
        last_name_lookup = '__'.join([name, 'last_name', 'contains'])
        return queryset.filter(
            Q(**{first_name_lookup: value}) | Q(**{last_name_lookup: value})
        )
