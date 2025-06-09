from django.urls import path

from .views import (
    index,
    PositionListView,
    WorkerListView,
    TaskListView,
    TeamListView,
    ProjectListView,
    WorkerCreateView,
    # WorkersUpdateView,
    # WorkersDeleteView,
    WorkerDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("position/", PositionListView.as_view(), name="position_list"),
    path("workers/", WorkerListView.as_view(), name="worker_list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    # path("workers/<int:pk>/update/", WorkersUpdateView.as_view(), name="worker-update"),
    # path("workers/<int:pk>/delete/", WorkersDeleteView.as_view(), name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("teams/", TeamListView.as_view(), name="team_list"),
    path("projects/", ProjectListView.as_view(), name="project_list"),

]

app_name = "task"
