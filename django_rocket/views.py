from django.conf import settings
from django.db import transaction
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import ConfirmRedeemInvitation, InvitationTokenCheckForm, SubscriberForm
from .models import InvitationToken
from .signals import new_subscriber, valid_token


class InvitationView(generic.FormView):
    template_name = 'django_rocket/request_invitation.html'
    form_class = SubscriberForm

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()

        new_subscriber.send(
            sender=self.__class__,
            request=self.request,
            subscriber=self.object)

        return HttpResponseRedirect(reverse('django_rocket:request_invitation_completed'))


class InvitationCompletedView(generic.TemplateView):
    template_name = 'django_rocket/request_invitation_completed.html'


class RequestAccessView(generic.FormView):
    template_name = 'django_rocket/request_access.html'
    form_class = InvitationTokenCheckForm

    @transaction.atomic
    def form_valid(self, form):
        token = form.use_token()

        valid_token.send(sender=self.__class__, request=self.request, token=token)
        response = HttpResponseRedirect(settings.LOGIN_URL)
        response.set_signed_cookie('invite', token.token, max_age=None)

        return response


class RequestAccessCompletedView(generic.TemplateView):
    template_name = 'django_rocket/request_access_completed.html'


class RedeemInvitationView(generic.View):
    template_name = 'django_rocket/request_access.html'
    form_class = ConfirmRedeemInvitation

    def dispatch(self, request, *args, **kwargs):
        try:
            self.token = InvitationToken.objects.get(token=kwargs['token'], uses__gte=1)
        except InvitationToken.DoesNotExist:
            return HttpResponseNotFound()
        return super(RedeemInvitationView, self).dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        self.token.uses -= 1
        self.token.save(update_fields=('uses',))

        valid_token.send(sender=self.__class__, request=self.request, token=self.token)

        response = HttpResponseRedirect(settings.LOGIN_URL)
        response.set_signed_cookie('invite', token.token, max_age=None)

        return response
