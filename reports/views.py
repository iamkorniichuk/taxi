from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from commons.decorators import perm_required
from commons.mixins import PermissionRequiredMixin

from .models import Report
from .apps import APP_NAME


class ReportListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Report
    template_name = APP_NAME + '/list.html'
    context_object_name = 'reports'

    required_perm = 'view_report'


@require_POST
@perm_required('accept_report')
def report_accept_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    report = Report.objects.get(pk=pk)
    report.manager = request.user
    report.save()

    # TODO: Provide valid url
    success_url = reverse(APP_NAME + ':detail', args=[pk])
    return HttpResponseRedirect(success_url)
