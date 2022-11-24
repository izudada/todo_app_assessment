from django.db import models
from django.urls import reverse


class Todo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('index')