import pytest
from rest_framework.test import APIClient



@pytest.fixture
def rest_api_client():
    return APIClient()

@pytest.mark.django_db
def test_guest_unauthorized_rest_framework_first_page(rest_api_client):
    response = rest_api_client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_guest_unauthorized_rest_framework_next_pages(rest_api_client):
    response = rest_api_client.get('singer')
    assert response.status_code == 404

@pytest.mark.django_db
def test_user_authorized_rest_framework_first_page(rest_api_client):
    rest_api_client.login(username='Usertest', password='usertest12345')
    response = rest_api_client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_authorized_rest_framework_next_page(rest_api_client):
    rest_api_client.login(username='Usertest', password='usertest12345')
    response = rest_api_client.get('http://localhost/singer/')
    assert response.status_code == 200
