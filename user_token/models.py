from django.db import models
from user.models import User
import uuid


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    token = models.CharField(
        max_length=36,
        unique=True,
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4(),
    )

    def __str__(self):
        return str(self.token)
