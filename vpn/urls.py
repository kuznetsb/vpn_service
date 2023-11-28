from django.urls import path

from vpn import views

urlpatterns = [
    path("sites/", views.SiteListView.as_view(), name="site-list"),
    path("sites/create/", views.SiteCreateView.as_view(), name="site-create"),
    path("sites/<int:pk>/detail/", views.SiteDetailView.as_view(), name="site-detail"),
    path("sites/<int:pk>/update/", views.SiteUpdateView.as_view(), name="site-update"),
    path("sites/<int:pk>/delete/", views.SiteDeleteView.as_view(), name="site-delete"),
]


app_name = "vpn"
