from optparse import make_option

from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.db import transaction
from django_rocket.models import InvitationToken


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--uses',
                    type="int",
                    dest='uses',
                    default=1,
                    help='Number of uses that this token will be enabled, set 1 if it will work just once,'
                         'No value to make it always enabled'),
    )

    @transaction.atomic
    def handle(self, *args, **options):
        token = InvitationToken.objects.create(uses=options.get('uses'))
        self.stdout.write('New token created, with pass code: {} and redeem url {}'.format(
            token.code,
            reverse('django_rocket:redeem_invitation', kwargs={'token': token.token})
        ))
