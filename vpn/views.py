from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import ModelFormMixin

from vpn.forms import SiteSearchForm, SiteNameUpdateForm, SiteCreateForm
from vpn.models import Site


@login_required
def index(request):
    """View function for the home page of the site."""

    context = {
        "num_all_tasks": 0,
        "num_tasks_done": 0,
        "num_workers": 0,
        "today_tasks": 0,
        "percentage": 0,
    }

    return render(request, "vpn/index.html", context=context)


class UserSitesMixin:
    def get_queryset(self):
        return Site.objects.filter(author=self.request.user)


class SiteListView(LoginRequiredMixin, UserSitesMixin, generic.ListView):
    model = Site
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = SiteSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        form = SiteSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class SiteDetailView(LoginRequiredMixin, UserSitesMixin, generic.DetailView):
    model = Site


class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Site
    success_url = reverse_lazy("vpn:site-list")
    form_class = SiteCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class SiteUpdateView(LoginRequiredMixin, UserSitesMixin, generic.UpdateView):
    model = Site
    form_class = SiteNameUpdateForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("vpn:site-detail", kwargs={"pk": pk})


class SiteDeleteView(LoginRequiredMixin, UserSitesMixin, generic.DeleteView):
    model = Site
    success_url = reverse_lazy("vpn:site-list")
