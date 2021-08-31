import datetime
from django.db import models
# Create your models here.


class TodoModel(models.Model):

    title = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())
