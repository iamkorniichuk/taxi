from django.core.validators import EMPTY_VALUES
from django_filters.filters import BooleanFilter


class EmptyStringFilter(BooleanFilter):
    def get_label(self):
        if self._label:
            return self._label
        else:
            result = "exclude " if self.exclude else ""
            result += f"empty {self.field_name}"
            return result.capitalize()

    def set_label(self, value):
        self._label = value

    label = property(get_label, set_label)

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.field_name: ""})
