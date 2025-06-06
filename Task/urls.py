from django.urls import path

from .views import index, PositionListView

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position-list"),
]

app_name = "task"
