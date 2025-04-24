from django.db import models

# Create your models here.
# core/models.py

from django.db import models
from django.conf import settings
from django.utils.timezone import now

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(default=now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="%(class)s_created_by"
    # )
    # updated_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="%(class)s_updated_by"
    # )

    class Meta:
        abstract = True
