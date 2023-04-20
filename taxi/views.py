from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRedirectView(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        home_url = None
        # TODO: To end
        if user.is_driver:
            home_url = user.driver.home_url
        elif user.is_customer:
            home_url = user.customer.home_url
        return home_url
