from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from users.forms import RegisterForm


class UserCreateView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("vpn:index")

    def form_valid(self, form):
        response = super().form_valid(form)

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)

        return response
