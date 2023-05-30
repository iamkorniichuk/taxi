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


def any_perm_required(*perms):
    def check_perms(user, *perms):
        for perm in perms:
            if user.has_perm(perm):
                return True
        return False
    return forbid_decorator(check_perms)
