from django.db import models


class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
