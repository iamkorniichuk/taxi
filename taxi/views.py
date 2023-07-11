from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            if user.has_perm("add_order"):
                url = "orders:create"
            else:
                url = "users:my_profile"
        else:
            url = "about"
        return reverse(url)


class AboutTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        from django.db.models import Avg, Count
        from django.db.models.functions import ExtractDay
        from django.utils import timezone

        from django.contrib.auth import get_user_model
        from trips.models import Trip
        from orders.models import Order

        User = get_user_model()

        data = super().get_context_data(**kwargs)
        data["customers_count"] = (
            User.objects.filter(groups__name="customer")
            .exclude(groups__name="driver")
            .count()
        )

        data["drivers_count"] = User.objects.filter(groups__name="driver").count()

        data["trips_count"] = (
            Trip.objects.exclude(complete_datetime__isnull=True).all().count()
        )

        data["avg_rating"] = round(
            Trip.objects.exclude(rating__isnull=True).aggregate(avg=Avg("rating"))[
                "avg"
            ],
            2,
        )

        current_month = timezone.now().month
        data["orders_per_day"] = int(
            Order.objects.filter(datetime__month=current_month)
            .annotate(day=ExtractDay("datetime"))
            .values("day")
            .annotate(count=Count("pk"))
            .aggregate(avg=Avg("count"))["avg"]
        )

        return data
