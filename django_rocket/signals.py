from django.contrib import messages
import django.dispatch

new_subscriber = django.dispatch.Signal(providing_args=["request", "subscriber"])
valid_token = django.dispatch.Signal(providing_args=["request", "subscriber"])


@django.dispatch.receiver(valid_token)
def alert_message(sender, **kwargs):
    request = kwargs['request']
    token = kwargs['token']

    tries_message = '. You have %d more uses for this token' % token.uses if token.uses >= 1 else ''
    messages.success(request, 'Welcome! you are giving access to our website%s' % tries_message)