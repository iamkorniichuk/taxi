from django.forms import Form, Textarea


class BootstrapForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            attrs = {"class": "form-control", "placeholder": field.label}
            if isinstance(field.widget, Textarea):
                attrs.update({"rows": "2"})
            field.widget.attrs.update(attrs)
            field.label = ""
            field.help_text = ""
