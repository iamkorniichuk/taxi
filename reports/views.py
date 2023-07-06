from django.utils import timezone
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from commons.decorators import perm_required
from commons.mixins import PermissionRequiredMixin
from commons.responses import refresh

from .models import Report
from .filter_sets import ReportFilterSet


class ReportListView(LoginRequiredMixin, FilterView):
    model = Report
    template_name = "reports/list.html"
    filterset_class = ReportFilterSet


# TODO: Restrict view for non related users
class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "reports/detail.html"


@require_POST
@perm_required("reports.answer_report")
def report_answer_view(request, *args, **kwargs):
    pk = request.POST.get("pk")
    answer = request.POST.get("answer")
    report = Report.objects.get(pk=pk)
    if not report.is_completed:
        report.answer = answer
        report.manager = request.user
        report.complete_datetime = timezone.now()
        report.save()

        return refresh(request)
