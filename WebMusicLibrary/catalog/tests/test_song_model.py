import pytest
from django.contrib.auth.models import User
from catalog.models import Song



@pytest.fixture
def create_user(db):
    return User.objects.create(username='Username', password='12345', email='Username@Username.com')

@pytest.fixture
def create_song(create_user):
    return Song.objects.create(name_song='TestNameSong', name_singer='TestNameSinger', title='TestAlbumTitle', number='3', author=create_user)


def test_authenticated_user_can_visit_page_song(client, create_user):
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Songs/')
    assert response.status_code == 200

def test_create_song_authenticated_user(client, create_user):
    assert Song.objects.count() == False
    Song.objects.create(name_song='TestNameSong', name_singer='TestNameSinger', title='TestAlbumTitle', number='3', author=create_user)
    assert Song.objects.count() != False

def test_params_song_model(create_song):
    assert create_song.name_song == 'TestNameSong'
    assert create_song.name_singer == 'TestNameSinger'
    assert create_song.title == 'TestAlbumTitle'
    assert create_song.number == '3'

def test_params_song_response_content(client, create_user, create_song):
    create_song
    client.force_login(create_user)
    response = client.get('http://localhost:8000/Songs/')
    assert b'TestNameSong' in response.content
    assert b'TestNameSinger' in response.content
    assert b'3' in response.content


@pytest.fixture
def song_first(create_user):
    return Song.objects.create(name_song='TestNameSong', name_singer='TestNameSinger', title='TestAlbumTitle-First', number='1', author=create_user)

@pytest.fixture
def song_second(create_user):
    return Song.objects.create(name_song='TestNameSong', name_singer='TestNameSinger', title='TestAlbumTitle-Second', number='3', author=create_user)

def test_song_comparison(song_first, song_second):
    assert song_first != song_second
