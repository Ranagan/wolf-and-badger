from django.urls import path

from users import views

urlpatterns = [
    path("", views.profile, name="profile_page"),
]
