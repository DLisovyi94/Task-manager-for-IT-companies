from django.urls import path

from .views import (
    index,
    PositionListView,
    WorkerListView,
    TaskListView,
    TeamListView,
    ProjectListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    WorkerDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "position/", PositionListView.as_view(),
        name="position_list"
    ),
    path("workers/",
         WorkerListView.as_view(),
         name="worker_list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/", WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path("workers/<int:pk>/update/",
         WorkerUpdateView.as_view(),
         name="worker-update"),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("teams/", TeamListView.as_view(), name="team_list"),
    path(
        "teams/<int:pk>/",
        TeamDetailView.as_view(),
        name="team-detail"
    ),
    path(
        "teams/create/",
        TeamCreateView.as_view(),
        name="team-create"
    ),
    path(
        "teams/<int:pk>/update/",
        TeamUpdateView.as_view(),
        name="team-update"
    ),
    path(
        "teams/<int:pk>/delete/",
        TeamDeleteView.as_view(),
        name="team-delete"
    ),
    path("projects/", ProjectListView.as_view(), name="project_list"),
    path(
        "projects/create/",
        ProjectCreateView.as_view(),
        name="project-create"
    ),
    path(
        "projects/<int:pk>/update/",
        ProjectUpdateView.as_view(),
        name="project-update"
    ),
    path(
        "projects/<int:pk>/delete/",
        ProjectDeleteView.as_view(),
        name="project-delete"
    ),
]

app_name = "task"
