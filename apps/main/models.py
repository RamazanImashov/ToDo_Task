from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class ToDo(models.Model):
    author = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username} -> {self.text}'