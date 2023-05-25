from django.urls import reverse
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        return reverse(user.groups[-1].home_url)
