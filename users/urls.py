from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("", include("django.contrib.auth.urls")),
    path("<int:pk>/", views.UserDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name="update"),
]

app_name = "users"
