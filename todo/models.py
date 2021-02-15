from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return self.title
