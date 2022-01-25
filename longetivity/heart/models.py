from django.db import models
import uuid

from django.db.models.deletion import CASCADE

class Details(models.Model):
    f_name = models.CharField(max_length=200, null=False, blank=False)
    l_name = models.CharField(max_length=200, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    tags = models.ManyToManyField('tags')
    age = models.IntegerField(default = 15, null=False, blank=False)
    profile_picture = models.ImageField(default = 'static/images/user.jpeg')
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, editable=False, unique = True, primary_key=True)

    def __str__(self) -> str:
        return self.username


class Tags(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, editable=False, unique = True, primary_key=True)

    def __str__(self) -> str:
        return self.name

class Votes(models.Model):
    votes = (
        ('+1', 'UPVOTE'),
        ('-1', 'DOWNVOTE')
    )
    name = models.CharField(max_length=200)
    relationship = models.ForeignKey(Details, on_delete=CASCADE)
    vote = models.IntegerField(choices= votes)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, editable=False, unique = True, primary_key=True)

    def __str__(self) -> str:
        return self.name