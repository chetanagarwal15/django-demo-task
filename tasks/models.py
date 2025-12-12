from django.db import models

class Task(models.Model):
    TODO = 'todo'
    INPROG = 'in-progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (INPROG, 'In Progress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
