from functools import wraps
from django.http import Http404

def allow_access_to(role_list):

    def decorator(func):

        @wraps(func)
        def inner(request, *args, **kwargs):

            if not request.user.id:
                raise Http404

            if role_list and request.user.role not in role_list:
                raise Http404

            return func(request, *args, **kwargs)

        return inner

    return decorator
