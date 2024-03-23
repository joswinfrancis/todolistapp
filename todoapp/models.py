from django.db import models
from django.utils import timezone

# Create your models here.
class TodoList(models.Model):
    title=models.CharField(max_length=200)
    details=models.TextField(max_length=200)
    date_time=models.DateTimeField(default=timezone.now,blank=True)

    def __str__(self):
        return self.title

