from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class Account(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='accounts')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'group'), name='unique account')
        ]

    def has_perm(self, perm: str) -> bool:
        return self.group.has_perm(perm)

    # TODO: To test
    @property
    def rating(self):
        return self.ratings.annotate(avg=models.Avg('pk'))['avg']
