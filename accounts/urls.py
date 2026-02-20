from django.urls import path
from .views import profile, profile_edit, profile_delete

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("delete/profile/", profile_delete, name="profile-delete"),
    path("edit/profile/", profile_edit, name="profile-edit")
]