from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>",views.entry, name="entry"),
    path("query/", views.query, name="query"),
    path("error/", views.error, name="error")
]
