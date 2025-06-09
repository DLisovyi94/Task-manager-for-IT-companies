from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import TextChoices


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.position})" if self.position else self.username


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "Urgent", "Urgent"
        HIGH = "High", "High"
        MEDIUM = "Medium", "Medium"
        LOW = "Low", "Low"

    priority = models.CharField(
        max_length=20, choices=Priority.choices, default=Priority.MEDIUM
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    task_type = models.ForeignKey(
        "TaskType", on_delete=models.PROTECT, related_name="tasks"
    )
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="assigned_tasks"
    )

    def __str__(self):
        return (
            f"{self.name}, "
            f"{self.task_type.name}, "
            f"priority: {self.priority}, "
            f"deadline: {self.deadline.strftime('%Y-%m-%d %H:%M')},"
            f"is_completed: {self.is_completed}"
        )


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    workers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="teams"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    team = models.ManyToManyField("Team", blank=True, related_name="projects")
    tasks = models.ManyToManyField("Task", related_name="projects", blank=True)

    def __str__(self):
        return f"project: {self.name}, description: {self.description}"


# Create your models here.
