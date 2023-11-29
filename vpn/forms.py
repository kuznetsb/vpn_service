from django import forms
from django.core.exceptions import ValidationError

from vpn.models import Site, Statistics


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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def clean(self):
        url_data = self.cleaned_data["url"]
        unified_url = url_data.strip("/").replace("https", "http")
        if Site.objects.filter(url=unified_url, author=self.request.user).exists():
            raise ValidationError("You already added this site")

        self.cleaned_data["url"] = unified_url
        return self.cleaned_data

    def save(self, commit=True):
        self.instance = super().save(commit=False)
        self.instance.author = self.request.user
        self.instance.save()

        Statistics.objects.create(site=self.instance)

        return self.instance


class SiteNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["name"]
