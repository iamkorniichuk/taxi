from django.urls import reverse
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.has_perm('add_order'):
            url = 'orders:create'
        else:
            url = 'users:my_profile'
        return reverse(url)
