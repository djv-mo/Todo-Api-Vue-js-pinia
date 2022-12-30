from django.db import models
from django.conf import settings
from django.http import request

class Task(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)

    created = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    fav = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
