from unittest import mock

import pytest


@pytest.mark.django_db
@mock.patch("django_rocket.models.uuid4")
@mock.patch("django_rocket.models.get_random_string")
def test_invitation_tokens(get_random_string, uuid4):
    get_random_string.return_value = "CODE"
    uuid4.return_value.hex = "TOKEN"

    from django_rocket.models import InvitationToken

    obj = InvitationToken.objects.create()

    assert obj.code == "CODE"
    assert obj.token == "TOKEN"
