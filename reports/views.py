from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Report
from .apps import APP_NAME


class AcceptReportView(LoginRequiredMixin, ListView):
    model = Report
    template_name = APP_NAME + '/accept_list.html'
    context_object_name = 'reports'
    success_accept_url = ''

    def get_queryset(self):
        return [report for report in self.model.objects.all() if report.is_open]

    def post(self, request, *args, **kwargs):
        report_pk = request.POST.get('report_pk', None)
        report = Report.objects.filter(pk=report_pk).first()
        report.manager = request.user.manager
        report.save()
        return HttpResponseRedirect(reverse_lazy(self.success_accept_url, args=[report_pk]))
