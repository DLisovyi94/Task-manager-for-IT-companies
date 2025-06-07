from django.urls import path

from .views import index, PositionListView, WorkerListView, TaskListView, TeamListView

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position_list"),
    path("workers/", WorkerListView.as_view(), name="worker_list"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("teams/", TeamListView.as_view(), name="team_list"),



]

app_name = "task"
