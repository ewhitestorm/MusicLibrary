"""WebMusicLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, re_path, include
from catalog import views
import catalog.views


schema_view = get_swagger_view(title='Music Library API')

urlpatterns = [
    re_path(r'^$', catalog.views.home, name='home'),
    path('index/', catalog.views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    re_path(r'^Albums/$', views.AlbumListView.as_view(), name='Albums'),
    re_path(r'^Singers/$', views.SingerListView.as_view(), name='Singers'),
    re_path(r'^Songs/$', views.SongListView.as_view(), name='Songs'),

    path('admin/', admin.site.urls, name='admin'),
    path('swagger/', schema_view),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('album/', views.AlbumList.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),
    path('singer/', views.SingerList.as_view()),
    path('singer/<int:pk>/', views.SingerDetail.as_view()),
    path('song/', views.SongList.as_view()),
    path('song/<int:pk>/', views.SongDetail.as_view()),
]
