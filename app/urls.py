from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", views.non_cached, name="non_cached"),
    path("localmemory-cached/", views.localmemory_cached, name="localmemory_cached"),
    path("filesystem-cached/", views.filesystem_cached, name="filesystem_cached"),
    path("database-cached/", views.database_cached, name="database_cached"),
    path("dummy-cached/", views.dummy_cached, name="dummy_cached"),
]