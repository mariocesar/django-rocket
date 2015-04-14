from re import compile

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import InvitationToken

INVITATION_EXEMPT_URLS = [
    compile(r'^%s/?' % reverse('django_rocket:request_invitation').lstrip('/')),
    compile(r'^%s/?' % reverse('django_rocket:request_invitation_completed').lstrip('/')),
    compile(r'^%s/?' % reverse('django_rocket:request_access').lstrip('/')),
]

if hasattr(settings, 'INVITATION_EXEMPT_URLS'):
    INVITATION_EXEMPT_URLS += [compile(expr) for expr in settings.INVITATION_EXEMPT_URLS]


class InvitationOnlyMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'user'), 'InvitationOnlyMiddleware must be added after the Session middleware'

        if not self.is_allowed_url(request.path_info):
            if InvitationToken.objects.filter(
                    token=request.get_signed_cookie(key='invite', default=None),
                    uses__gte=1).exists():
                return
            return HttpResponseRedirect(reverse('django_rocket:request_invitation'))

    def is_allowed_url(self, path):
        path = path.lstrip('/')
        return any(m.match(path) for m in INVITATION_EXEMPT_URLS)