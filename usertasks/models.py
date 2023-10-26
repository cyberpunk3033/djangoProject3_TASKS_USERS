from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(AbstractUser):
    email = models.EmailField()
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)


class Task(models.Model):
    STATUS_CHOICES = (
        ('В ожидании', 'В ожидании'),
        ('В процессе', 'В процессе'),
        ('Завершено', 'Завершено'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField()

    def __str__(self):
        return self.title