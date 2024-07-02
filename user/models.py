from django.db import models


class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Token(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Token')
    token = models.CharField(max_length=16)

    def __str__(self):
        return str(self.username)