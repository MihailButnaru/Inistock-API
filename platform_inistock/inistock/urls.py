from django.urls import path

from inistock.views import PersonViewSet, ShareViewSet

urlpatterns = [
    path(
        "person",
        PersonViewSet.as_view(actions={"post": "create"}),
        name="person-details",
    ),
    path(
        "person/<int:person_id>",
        PersonViewSet.as_view(actions={"patch": "update", "get": "retrieve"}),
        name="person-info",
    ),
    path(
        "share",
        ShareViewSet.as_view(actions={"post": "create", "get": "list"}),
        name="share-details",
    ),
    path(
        "share/<int:share_id>",
        ShareViewSet.as_view(actions={"patch": "update", "get": "retrieve", "delete": "delete"}),
        name="share-info",
    ),
]
