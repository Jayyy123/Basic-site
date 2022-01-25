from typing_extensions import runtime
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null= False)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    sex = models.CharField(max_length=6)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key= True, editable = False, unique=True)

    def __str__(self) -> str:
        return self.username