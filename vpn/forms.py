from django import forms

from vpn.models import Site


class SiteSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by site name..."}),
    )


class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["name", "url"]


class SiteNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["name"]
