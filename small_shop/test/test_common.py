import pytest


@pytest.mark.django_db
def test_dummy(client):
    assert 1 == 2
