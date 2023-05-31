from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from commons.decorators import perm_required
from commons.mixins import PermissionRequiredMixin

from .models import Report
from .forms import ReportAnswerForm
from .apps import APP_NAME


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Report
    template_name = APP_NAME + '/list.html'
    context_object_name = 'reports'

    required_perm = 'view_report'


# TODO: Restrict view for non related users
class ReportDetailView(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = APP_NAME + '/detail.html'
    form_class = ReportAnswerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['report'] = self.get_object()
        return data

    @method_decorator(perm_required('answer_report'))
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if not self.get_object().is_completed:
            user = self.request.user
            instance = form.save(commit=False)
            instance.manager = user
            instance.complete_datetime = timezone.now()
            instance.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return self.object.get_absolute_url()


@require_POST
@perm_required('answer_report')
def report_answer_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    report = Report.objects.get(pk=pk)
    report.manager = request.user
    report.save()

    # TODO: Provide valid url
    success_url = reverse(APP_NAME + ':detail', args=[pk])
    return HttpResponseRedirect(success_url)
