from django.db import models
from datetime import datetime


class Todos(models.Model):
    title = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
