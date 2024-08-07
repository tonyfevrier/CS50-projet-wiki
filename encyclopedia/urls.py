from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>",views.entry, name="entry"),
    path("query/", views.query, name="query"), 
    path("newpage/", views.newpage, name="newpage"),
    path("savenewpage/", views.savenewpage, name="savenewpage"),
    path("wiki/<str:TITLE>/edit", views.editpage, name="editpage"),
    path("wiki/<str:TITLE>/saveedition", views.saveedition, name="saveedition"),
]
