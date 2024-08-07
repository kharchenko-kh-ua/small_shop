"""
Test fixtures/
"""
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="testuser", password="testpass")
    return user


@pytest.fixture
def auth_client(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    return api_client


@pytest.fixture
def admin_client(api_client, test_user):
    test_user.is_admin = True
    test_user.is_staff = True
    test_user.save()
    api_client.force_authenticate(user=test_user)
    return api_client
