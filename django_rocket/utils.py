from django.utils.crypto import salted_hmac


def create_token(value):
    return salted_hmac('rocket', value).hexdigest()
