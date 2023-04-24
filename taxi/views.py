from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.modes import get_mode


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        request = self.request
        profile_mode = get_mode(request)
        return profile_mode.home_url
