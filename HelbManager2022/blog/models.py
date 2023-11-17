from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.TextField()
    project_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Task(models.Model):
    name = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
        ('in_revision', 'In Revision'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Subtask(models.Model):
    name = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
        ('in_revision', 'In Revision'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

