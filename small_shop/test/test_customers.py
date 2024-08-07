"""
Tests.
"""
from unittest.mock import ANY

import pytest
from api.models import Customer


@pytest.mark.django_db
def test_non_authenticated_user_can_access_user_endpoint(client):
    url = "/api/customers/"

    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_crud_customer(auth_client):
    url = "/api/customers/"

    # Create
    response = auth_client.post(
        url,
        data={
            "first_name": "new_user_first_name",
            "last_name": "new_user_last_name",
        },
    )
    assert response.status_code == 201
    customer = Customer.objects.filter(first_name="new_user_first_name")
    assert customer.exists()

    # Read
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.json()[0] == {
        "id": ANY,
        "first_name": "new_user_first_name",
        "last_name": "new_user_last_name",
        "photo": None,
    }

    # Update
    customer_id = customer.get().id
    response = auth_client.patch(
        url + str(customer_id) + "/",
        data={
            "first_name": "new_user_first_name_updated",
            "last_name": "new_user_last_name_updated",
        },
    )
    assert response.status_code == 200
    customer = Customer.objects.get(id=customer_id)
    assert customer.first_name == "new_user_first_name_updated"
    assert customer.modified_by == auth_client.handler._force_user

    # Delete
    response = auth_client.delete(url + str(customer_id) + "/")
    assert response.status_code == 204
    assert not Customer.objects.filter(id=customer_id).exists()
