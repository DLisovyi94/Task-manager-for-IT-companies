from django import forms
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from task.models import Worker, Position, Task, Team


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "position")


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]


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


# def validate_license_number(
#     license_number,
# ):  # regex validation is also possible here
#     if len(license_number) != 8:
#         raise ValidationError("License number should consist of 8 characters")
#     elif not license_number[:3].isupper() or not license_number[:3].isalpha():
#         raise ValidationError("First 3 characters should be uppercase letters")
#     elif not license_number[3:].isdigit():
#         raise ValidationError("Last 5 characters should be digits")
#
#     return license_number
#
#
# class DriverSearchForm(forms.Form):
#     username = forms.CharField(
#         max_length=255,
#         required=False,
#         label="",
#         widget=forms.TextInput(
#             attrs={"placeholder": "search by Username"})
#     )
#
#
# class CarSearchForm(forms.Form):
#     model = forms.CharField(
#         max_length=255,
#         required=False,
#         label="",
#         widget=forms.TextInput(
#             attrs={"placeholder": "search by Model"})
#     )
#
#
# class ManufacturerSearchForm(forms.Form):
#     name = forms.CharField(
#         max_length=255,
#         required=False,
#         label="",
#         widget=forms.TextInput(
#             attrs={"placeholder": "search by Name"})
#     )
