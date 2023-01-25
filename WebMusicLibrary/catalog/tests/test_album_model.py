import pytest
from django.contrib.auth.models import User
from catalog.models import Album



@pytest.fixture
def create_user(db):
    return User.objects.create(username='Username', password='12345', email='Username@Username.com')

@pytest.fixture
def create_album(create_user):
    return Album.objects.create(title='TestAlbumTitle', name_singer='TestNameSinger', release_date='2010', author=create_user)


def test_authenticated_user_can_visit_page_album(client, create_user):
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Albums/')
    assert response.status_code == 200

def test_create_album_authenticated_user(client, create_user):
    assert Album.objects.count() == False
    Album.objects.create(title='TestAlbumTitle', name_singer='TestNameSinger', release_date='2010', author=create_user)
    assert Album.objects.count() != False

def test_params_album_model(create_album):
    assert create_album.title == 'TestAlbumTitle'
    assert create_album.name_singer == 'TestNameSinger'
    assert create_album.release_date == '2010'

def test_params_album_response_content(client, create_user, create_album):
    create_album
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Albums/')
    assert b'TestAlbumTitle' in response.content
    assert b'TestNameSinger' in response.content
    assert b'2010' in response.content


@pytest.fixture
def album_1991(create_user):
    return Album.objects.create(title='TestAlbumTitle', name_singer='TestNameSinger', release_date='1991', author=create_user)

@pytest.fixture
def album_2022(create_user):
    return Album.objects.create(title='TestAlbumTitle', name_singer='TestNameSinger', release_date='2022', author=create_user)

def test_album_comparison(album_1991, album_2022):
    assert album_1991 != album_2022
