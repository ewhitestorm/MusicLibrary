import pytest
from django.contrib.auth.models import User



@pytest.fixture
def create_user(django_user_model):
    return django_user_model.objects.create(username='Usertest', password='usertest12345')


def test_authenticated_user(client, create_user):
    client.force_login(create_user)
    response = client.get('http://localhost/Albums/')
    assert response.status_code == 200

def test_user_model_create(django_user_model, create_user):
    assert create_user.username == 'Usertest'
    assert create_user.password == 'usertest12345'
    assert django_user_model.objects.count() == True

@pytest.mark.django_db
def test_check_password():
    user = User.objects.create_user(username='Usertest')
    user.set_password('password')
    assert user.check_password('password') is True


@pytest.fixture
def user_first(db):
    return User.objects.create(username='Username1', password='12345', email='Username1@Username1.com')

@pytest.fixture
def user_second(db):
    return User.objects.create(username='Username2', password='54321', email='Username2@Username2.com')

def test_user_comparison(user_first, user_second):
    assert user_first != user_second
