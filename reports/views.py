from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from commons.decorators import any_perm_required

from .models import Report
from .apps import APP_NAME


class ReportAcceptView(LoginRequiredMixin, ListView):
    model = Report
    template_name = APP_NAME + '/accept_list.html'
    context_object_name = 'reports'
    success_accept_url = ''

    # TODO: Improve performance
    def get_queryset(self):
        return [report for report in self.model.objects.all() if report.is_open]

    @method_decorator(any_perm_required(APP_NAME + '.accept_' + model.__name__))
    def post(self, request, *args, **kwargs):
        report_pk = request.POST.get('report_pk', None)
        report = Report.objects.filter(pk=report_pk).first()
        report.manager = request.user.manager
        report.save()
        return HttpResponseRedirect(reverse_lazy(self.success_accept_url, args=[report_pk]))
