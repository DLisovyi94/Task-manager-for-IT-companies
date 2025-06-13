from django.test import TestCase
from django.utils import timezone
from task.forms import (
    WorkerCreationForm, WorkerUpdateForm, TaskCreationForm,
    TeamCreationForm, ProjectCreationForm,
    WorkerSearchForm, TaskSearchForm, TeamSearchForm, ProjectSearchForm
)
from task.models import Position, TaskType, Tag, Team
from django.contrib.auth import get_user_model


class FormTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Coding")
        self.tag = Tag.objects.create(name="Backend")
        self.worker = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            position=self.position
        )

    def test_worker_creation_form_valid(self):
        form = WorkerCreationForm(data={
            "username": "newuser",
            "first_name": "Jane",
            "last_name": "Doe",
            "password1": "complexpassword123",
            "password2": "complexpassword123",
            "position": self.position.id
        })
        self.assertTrue(form.is_valid())

    def test_worker_update_form_valid(self):
        form = WorkerUpdateForm(data={
            "first_name": "Updated",
            "last_name": "User",
            "position": self.position.id
        }, instance=self.worker)
        self.assertTrue(form.is_valid())

    def test_task_creation_form_valid(self):
        form = TaskCreationForm(data={
            "name": "Fix Bug",
            "description": "Fix critical issue",
            "task_type": self.task_type.id,
            "priority": "High",
            "deadline": timezone.now() + timezone.timedelta(days=1),
            "is_completed": False,
            "assignees": [self.worker.id],
            "tags": [self.tag.id],
        })
        self.assertTrue(form.is_valid())

    def test_team_creation_form(self):
        form = TeamCreationForm(
            data={"name": "Dev Team", "workers": [self.worker.id]})
        self.assertTrue(form.is_valid())

    def test_project_creation_form(self):
        team = Team.objects.create(name="QA Team")
        team.workers.add(self.worker)
        form = ProjectCreationForm(data={
            "name": "Project X",
            "description": "Big project",
            "team": [team.id]
        })
        self.assertTrue(form.is_valid())

    def test_worker_search_form(self):
        form = WorkerSearchForm(data={"position": "Developer"})
        self.assertTrue(form.is_valid())

    def test_task_search_form(self):
        form = TaskSearchForm(data={"name": "Bug"})
        self.assertTrue(form.is_valid())

    def test_team_search_form(self):
        form = TeamSearchForm(data={"name": "Team"})
        self.assertTrue(form.is_valid())

    def test_project_search_form(self):
        form = ProjectSearchForm(data={"name": "Project"})
        self.assertTrue(form.is_valid())
