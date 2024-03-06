"""
Tasks models
"""
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{"✔" if self.is_done else "⏲"} - {self.title}"
