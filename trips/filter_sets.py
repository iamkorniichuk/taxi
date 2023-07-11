from django.db.models import Q
from django.forms import TextInput
from django_filters.filters import CharFilter, BooleanFilter, OrderingFilter

from commons.filters.filter_sets import BootstrapFilterSet
from commons.filters.widgets import SelectBooleanWidget

from .models import Trip


class TripFilterSet(BootstrapFilterSet):
    class Meta:
        model = Trip
        fields = "__all__"
        exclude = ("order", "start_datetime", "complete_datetime")

    ordering = OrderingFilter(
        fields=[("start_datetime", "start_datetime")], empty_label=None, null_label=None
    )

    driver = CharFilter(
        field_name="driver", method="find_by_full_name", widget=TextInput
    )
    is_completed = BooleanFilter(
        field_name="is_completed", label="Is completed", widget=SelectBooleanWidget
    )
    has_report = BooleanFilter(
        field_name="has_report", label="Has report", widget=SelectBooleanWidget
    )

    @property
    def qs(self):
        queryset = super().qs
        user = self.request.user
        if not user.has_perm("trips.view_trip"):
            queryset = queryset.filter(Q(driver=user) | Q(order__customer=user))
        return queryset

    def find_by_full_name(self, queryset, name, value):
        first_name_lookup = "__".join([name, "first_name", "contains"])
        last_name_lookup = "__".join([name, "last_name", "contains"])
        return queryset.filter(
            Q(**{first_name_lookup: value}) | Q(**{last_name_lookup: value})
        )
