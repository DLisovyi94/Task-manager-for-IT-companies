
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task.models import Worker, Task, Team, Project


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "position")

    # def clean_position(self):
    #     return validate_position(self.cleaned_data["position"])


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]

    # def clean_position(self):
    #     return validate_position(self.cleaned_data["position"])


# def validate_position(position):
#     if not position.name.isalpha():
#         raise ValidationError(
#             "Position should contain only letters and "
#             "no digits or symbols.")
#     return position


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "task_type",
            "assignees",
            "priority",
            "deadline",
            "is_completed",
            "tags",
        ]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["assignees", "is_completed", "tags"]


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["team", "tasks"]


class WorkerSearchForm(forms.Form):
    position = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search by Position"})
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search by Task name"})
    )


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search by Team name"})
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search by Project name"})
    )
