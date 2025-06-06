from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from task.models import Position, Worker, TaskType, Task, Tag, Team, Project


@login_required
def index(request):
    """View function for the home page of the site."""

    position = Position.objects.all()
    worker = Worker.objects.all()
    tasktypes = TaskType.objects.all()
    task = Task.objects.all()
    tags = Tag.objects.all()
    team = Team.objects.all()
    projects = Project.objects.all()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "position": position,
        "worker": worker,
        "tasktypes": tasktypes,
        "task": task,
        "tags": tags,
        "team": team,
        "projects": projects,
        "num_visits": num_visits + 1,
    }

    return render(request, 'task/index.html', context=context)


class PositionListView(LoginRequiredMixin,ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task/position_list.html"
    paginate_by = 5

class WorkerListView(LoginRequiredMixin,ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task/worker_list.html"
    paginate_by = 5


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5


# Create your views here.
