from functools import wraps

from django.core.exceptions import PermissionDenied


def forbid_decorator(test_func):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapped_view
    return decorator


def perm_required(perm):
    def check_perm(user, perm=None):
        return user.has_perm(perm)
    return forbid_decorator(check_perm)
