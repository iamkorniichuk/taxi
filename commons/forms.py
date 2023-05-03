from django.forms import Form


class BootstrapForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control', 'placeholder': field.label})
            field.label = ''
            field.help_text = ''
