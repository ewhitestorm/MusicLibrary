import pytest
from django.contrib.auth.models import User
from catalog.models import Singer



@pytest.fixture
def create_user(db):
    return User.objects.create(username='Username', password='12345', email='Username@Username.com')

@pytest.fixture
def create_singer(create_user):
    return Singer.objects.create(name_singer='TestNameSinger', author=create_user)


def test_authenticated_user_can_visit_page_singer(client, create_user):
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Singers/')
    assert response.status_code == 200

def test_create_singer_authenticated_user(client, create_user):
    assert Singer.objects.count() == False
    Singer.objects.create(name_singer='TestNameSinger', author=create_user)
    assert Singer.objects.count() != False

def test_params_singer_model(create_singer):
    assert create_singer.name_singer == 'TestNameSinger'

def test_params_singer_response_content(client, create_user, create_singer):
    create_singer
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Singers/')
    assert b'TestNameSinger' in response.content


@pytest.fixture
def singer_first(create_user):
    return Singer.objects.create(name_singer='TestNameSinger-First', author=create_user)

@pytest.fixture
def singer_second(create_user):
    return Singer.objects.create(name_singer='TestNameSinger-Second', author=create_user)

def test_singer_comparison(singer_first, singer_second):
    assert singer_first != singer_second
