from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView

from task.forms import (
    WorkerCreationForm,
    WorkerUpdateForm,
    TaskCreationForm,
    TaskUpdateForm,
    TeamCreationForm,
    TeamUpdateForm,
    ProjectCreationForm,
    ProjectUpdateForm,
    WorkerSearchForm,
    TaskSearchForm,
    TeamSearchForm,
    ProjectSearchForm
)
from task.models import (
    Position,
    Worker,
    TaskType,
    Task,
    Tag,
    Team,
    Project
)


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
        "position_list": position,
        "worker_list": worker,
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
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        position = self.request.GET.get("position", "")
        context["position"] = position
        context["search_form"] = WorkerSearchForm(
            initial={"position": position}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                position__name__icontains=form.cleaned_data["position"])
        return queryset


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
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TaskSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.select_related(
            "task_type").prefetch_related("assignees", "tags")
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task_list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task_list")


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "team_list"
    template_name = "task/team_list.html"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TeamSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Team.objects.all()
        form = TeamSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"])
        return queryset


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    context_object_name = "team"
    template_name = 'task/team_detail.html'


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamCreationForm
    template_name = "task/team_form.html"
    success_url = reverse_lazy("task:team_list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamUpdateForm
    template_name = "task/team_form.html"
    success_url = reverse_lazy("task:team_list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("task:team_list")


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "task/project_list.html"
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = ProjectSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Project.objects.prefetch_related("tasks")
        form = ProjectSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "task/project_form.html"
    success_url = reverse_lazy("task:project_list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = "task/project_form.html"
    success_url = reverse_lazy("task:project_list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("task:task_list")
