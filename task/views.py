from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView

from task.forms import WorkerCreationForm, WorkerUpdateForm, TaskCreationForm, TaskUpdateForm
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

    return render(request, "task/index.html", context=context)


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task/position_list.html"
    paginate_by = 2


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task/worker_list.html"
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    context_object_name = "worker"
    template_name = "task/worker_detail.html"


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "task/worker_form.html"
    success_url = reverse_lazy("task:worker_list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task:worker_list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task:worker_list")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # <-- обов'язково
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("task:worker_list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task:worker_list")


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "team_list"
    template_name = "task/team_list.html"
    paginate_by = 5


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "task/project_list.html"
    paginate_by = 5


# Create your views here.
