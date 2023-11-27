from django.urls import reverse_lazy
from django.views import generic

from users.forms import RegisterForm


class UserCreateView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:logout")
