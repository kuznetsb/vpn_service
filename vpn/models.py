from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sites"
    )

    class Meta:
        unique_together = [("url", "author")]


class Statistics(models.Model):
    site = models.OneToOneField(
        Site, on_delete=models.CASCADE, related_name="statistics"
    )
    transitions_number = models.PositiveIntegerField(default=0)
    data_volume_upload = models.FloatField(
        help_text="Обʼєм даних який було відправлено (в МБ)",
        default=0.0,
        validators=[MinValueValidator(0.0)],
    )
    data_volume_downloaded = models.FloatField(
        help_text="Обʼєм даних який було завантажено (в МБ)",
        default=0.0,
        validators=[MinValueValidator(0.0)],
    )
