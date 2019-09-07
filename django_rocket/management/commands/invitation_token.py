from django.core.management.base import BaseCommand
from django.db import transaction
from django.urls import reverse

from django_rocket.models import InvitationToken


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--uses',
            type="int",
            dest='uses',
            default=1,
            help='Number of uses that this token will be enabled, set 1 if it will work just once,'
                 'No value to make it always enabled'),

    @transaction.atomic
    def handle(self, *args, **options):
        token = InvitationToken.objects.create(uses=options.get('uses'))
        self.stdout.write('New token created, with pass code: {} and redeem url {}'.format(
            token.code,
            reverse('django_rocket:redeem_invitation', kwargs={'token': token.token})
        ))
