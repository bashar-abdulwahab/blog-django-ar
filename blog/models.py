from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# pyhon mange.py sqlmigrate blog 0001
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-post_date',)






