from .models import ACCOUNTS


def get_account(user, name):
    return getattr(user, name, False)


def set_mode(request, name) -> bool:
    if name in map(lambda a: a.model_name, ACCOUNTS):
        request.session['mode'] = name
        request.session.create()
        return True
    return False


def set_default_mode(request):
    for account in reversed(ACCOUNTS):
        name = account.model_name
        if get_account(request.user, name):
            set_mode(request, name)
            break


def get_mode(request):
    mode = request.session.get('mode', False)
    if mode:
        return get_account(request.user, mode)
    set_default_mode(request)
    return get_mode(request)


def get_all_modes(user):
    modes = []
    for account in ACCOUNTS:
        mode = get_account(user, account.model_name)
        if mode:
            modes.append(mode)
    return modes
