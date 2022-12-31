from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    fav = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
