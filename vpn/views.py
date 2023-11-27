from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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
