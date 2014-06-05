from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')
        ordering = ('-created',)

    def __str__(self):
        return self.email
