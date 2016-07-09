from django.db import models

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=512, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title
# Create your models here.
