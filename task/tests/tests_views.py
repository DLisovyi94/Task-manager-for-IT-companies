from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from task.models import Position, TaskType, Task, Team, Project


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
            position=self.position
        )
        self.task_type = TaskType.objects.create(name="Feature")
        self.task = Task.objects.create(
            name="Test Task",
            description="Some description",
            deadline=timezone.now() + timezone.timedelta(days=3),
            task_type=self.task_type,
            created_by=self.user
        )
        self.task.assignees.add(self.user)

        self.team = Team.objects.create(name="Dev Team")
        self.team.workers.add(self.user)

        self.project = Project.objects.create(
            name="My Project",
            description="Project desc")
        self.project.team.add(self.team)
        self.project.tasks.add(self.task)

    def test_login_required_redirect(self):
        response = self.client.get(
            reverse("task:worker_list"))
        self.assertRedirects(
            response, f"/accounts/login/?next={reverse('task:worker_list')}")

    def test_index_view_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("task:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/index.html")
        self.assertIn("worker_list", response.context)
        self.assertIn("task", response.context)
        self.assertIn("projects", response.context)

    def test_worker_list_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("task:worker_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/worker_list.html")

    def test_task_list_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("task:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_team_list_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("task:team_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dev Team")

    def test_project_list_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("task:project_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Project")
