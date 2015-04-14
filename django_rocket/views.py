from django.views import generic
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import transaction

from .forms import SubscriberForm, InvitationTokenCheckForm
from .signals import new_subscriber, valid_token


class RequestInvitationView(generic.FormView):
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


class RequestAccessCompletedView(generic.FormView):
    template_name = 'django_rocket/request_access.html'
    form_class = InvitationTokenCheckForm

    @transaction.atomic
    def form_valid(self, form):
        token = form.use_token()
        valid_token.send(
            sender=self.__class__,
            request=self.request,
            token=token)
        return HttpResponseRedirect(settings.LOGIN_URL)


class RequestInvitationCompletedView(generic.TemplateView):
    template_name = 'django_rocket/request_invitation_completed.html'