from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from django_rocket.utils import create_token


class Subscriber(models.Model):
    first_name = models.CharField(max_length=140, blank=True)
    last_name = models.CharField(max_length=140, blank=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')
        ordering = ('-created',)

    def __str__(self):
        return self.email


class InvitationToken(models.Model):
    code = models.CharField(max_length=12, unique=True, blank=True)
    token = models.CharField(max_length=40, unique=True, editable=False)

    uses = models.PositiveIntegerField(
        default=1, blank=True, null=True,
        help_text='Number of uses that this token will be enabled, set 1 if it will work just once,'
                  'No value to make it always enabled')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created)

    def save(self, **kwargs):
        if not self.id:
            if not self.code:
                self.code = get_random_string()
        self.token = create_token(self.code)
        return super(InvitationToken, self).save(**kwargs)
