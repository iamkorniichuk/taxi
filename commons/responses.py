from django.shortcuts import redirect


def refresh(request):
    return redirect(request.META["HTTP_REFERER"])
