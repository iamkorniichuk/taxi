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


def group_required(group):
    def check_group(user, *args, **kwargs):
        return user.has_group(group)
    return forbid_decorator(check_group)
