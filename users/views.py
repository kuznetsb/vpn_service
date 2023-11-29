from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic

from users.forms import RegisterForm, UserUpdateForm
from vpn.models import Statistics


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


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    queryset = get_user_model().objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_statistics = Statistics.objects.select_related("site__author").filter(
            site__author=self.request.user
        )
        context["sites_stats"] = user_statistics
        return context


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("users:detail", kwargs={"pk": pk})
