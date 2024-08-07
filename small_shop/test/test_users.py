"""
Tests.
"""
from unittest.mock import ANY

import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_non_admin_user_access(auth_client):
    url = "/api/users/"

    response = auth_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_crud_users(admin_client):
    url = "/api/users/"

    # Create
    response = admin_client.post(
        url,
        data={
            "username": "test",
            "first_name": "new_user_first_name",
            "last_name": "new_user_last_name",
            "password": "AbsolutelySafeP@ssword!",
        },
    )
    assert response.status_code == 201
    user = User.objects.filter(username="test")
    assert user.exists()

    # Read
    response = admin_client.get(url)
    assert response.status_code == 200
    assert response.json()[0] == {
        "id": ANY,
        "password": ANY,
        "last_login": ANY,
        "is_superuser": True,
        "username": "dev",
        "first_name": "",
        "last_name": "",
        "email": "dev@small-shop.com",
        "is_staff": True,
        "is_active": True,
        "date_joined": ANY,
        "groups": [],
        "user_permissions": [],
    }

    # Update (can change admin status)
    user_id = user.get().id
    response = admin_client.patch(
        url + str(user_id) + "/",
        data={
            "first_name": "new_user_first_name_updated",
            "last_name": "new_user_last_name_updated",
            "is_staff": True,
        },
    )
    assert response.status_code == 200
    user = User.objects.get(id=user_id)
    assert user.first_name == "new_user_first_name_updated"
    assert user.is_staff is True

    # Delete
    response = admin_client.delete(url + str(user_id) + "/")
    assert response.status_code == 204
    assert not User.objects.filter(id=user_id).exists()
