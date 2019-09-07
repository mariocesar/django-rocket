from re import compile

from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse

from .models import InvitationToken

INVITATION_EXEMPT_URLS = [
    compile(r'^%s/?' % reverse('django_rocket:request_invitation').lstrip('/')),
    compile(r'^%s/?' % reverse('django_rocket:request_invitation_completed').lstrip('/')),
    compile(r'^%s/?' % reverse('django_rocket:request_access').lstrip('/')),
]

if hasattr(settings, 'INVITATION_EXEMPT_URLS'):
    INVITATION_EXEMPT_URLS += [compile(expr) for expr in settings.INVITATION_EXEMPT_URLS]


def invitation_only_middleware(get_response):
    def is_allowed_url(path):
        path = path.lstrip('/')
        return any(m.match(path) for m in INVITATION_EXEMPT_URLS)

    def middleware(request):
        assert hasattr(request, 'user'), 'InvitationOnlyMiddleware must be added after the Session middleware'

        if not is_allowed_url(request.path_info):
            token = request.get_signed_cookie(key='invite', default=None)
            if InvitationToken.objects.filter(token=token, uses__gte=1).exists():
                return HttpResponseForbidden("Invitation required")
            return HttpResponseRedirect(reverse('django_rocket:request_invitation'))

        return get_response(request)

    return middleware
