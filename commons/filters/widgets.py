from django.forms.widgets import RadioSelect


class SelectBooleanWidget(RadioSelect):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.choices = (("true", "Yes"), ("false", "No"))

