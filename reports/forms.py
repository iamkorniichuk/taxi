from django.forms import ModelForm

from commons.forms import BootstrapForm

from .models import Report


class ReportAnswerForm(ModelForm, BootstrapForm):
    def __init__(self, *args, **kwargs):
        super(ReportAnswerForm, self).__init__(*args, **kwargs)
        self.fields["answer"].required = True

    class Meta:
        model = Report
        fields = ("answer",)
