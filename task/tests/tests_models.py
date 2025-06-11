from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from task.models import Position, Worker, TaskType, Task, Tag, Team, Project


class ModelsTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user1 = get_user_model().objects.create_user(
            username="user1",
            password="testpass123",
            first_name="Alice",
            last_name="Smith",
            position=self.position,
        )
        self.user2 = get_user_model().objects.create_user(
            username="user2",
            password="testpass456"
        )
        self.task_type = TaskType.objects.create(name="Bug")
        self.tag1 = Tag.objects.create(name="backend")
        self.tag2 = Tag.objects.create(name="urgent")
        self.task = Task.objects.create(
            name="Fix server error",
            description="Fix 500 error on server",
            deadline=timezone.now() + timezone.timedelta(days=2),
            task_type=self.task_type,
            created_by=self.user1,
            priority=Task.Priority.HIGH,
        )
        self.task.tags.add(self.tag1, self.tag2)
        self.task.assignees.add(self.user2)
        self.team = Team.objects.create(name="Backend Team")
        self.team.workers.add(self.user1, self.user2)
        self.project = Project.objects.create(
            name="Platform API", description="API development"
        )
        self.project.team.add(self.team)
        self.project.tasks.add(self.task)

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_worker_str(self):
        self.assertEqual(str(self.user1), "(Alice Smith - Developer )")
        self.assertEqual(str(self.user2), "user2")

    def test_worker_absolute_url(self):
        self.assertEqual(
            self.user1.get_absolute_url(),
            f"/workers/{self.user1.pk}/"
        )

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug")

    def test_tag_str(self):
        self.assertEqual(str(self.tag1), "backend")

    def test_task_str(self):
        expected_str = (
            f"{self.task.name}, {self.task_type.name}, priority: {self.task.priority}, "
            f"deadline: {self.task.deadline.strftime('%Y-%m-%d %H:%M')},"
            f"is_completed: {self.task.is_completed}"
        )
        self.assertEqual(str(self.task), expected_str)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Backend Team")

    def test_project_str(self):
        self.assertEqual(
            str(self.project),
            "project: Platform API, description: API development"
        )
