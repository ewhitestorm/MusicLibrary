import pytest
from django.urls import reverse
from django.contrib.auth.models import User



def test_guest_first_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_guest_index_page(client):
    response = client.get('Albums')
    assert response.status_code == 404

@pytest.mark.django_db
def test_user_first_page(admin_client):
    response = admin_client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_superuser(admin_client):
   url = reverse('Albums')
   response = admin_client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user(username='usertest', email='usertest@user.test', password='user_test12345')
    assert User.objects.count() == True
