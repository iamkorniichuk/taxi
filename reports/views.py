from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
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

    required_perm = APP_NAME + '.view_report'


# TODO: Restrict view for non related users
class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = APP_NAME + '/detail.html'


@require_POST
@perm_required(APP_NAME + '.answer_report')
def report_answer_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    report = Report.objects.get(pk=pk)
    if not report.is_completed:
        report.manager = request.user
        report.complete_datetime = timezone.now()
        report.save()

        return redirect(request.META['HTTP_REFERER'])
