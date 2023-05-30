from django.core.exceptions import PermissionDenied


class PermissionRequiredMixin(object):
    def check_perm(self):
        user = self.request.user
        perm = self.required_perm
        if not user.has_perm(perm):
            raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        self.check_perm()
        return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
