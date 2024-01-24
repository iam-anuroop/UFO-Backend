from django.db import models
from account.models import MyUser
import uuid


class Message(models.Model):
    sender = models.ForeignKey(MyUser, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(MyUser, related_name='receiver', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    group_admin = models.ForeignKey(MyUser, related_name='group_admin', on_delete=models.CASCADE)
    members = models.ManyToManyField(MyUser)


class BlockedUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='blocked_users')
    blocked_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'blocked_user')
        # thid unique_togetherensures that a user can only be blocked 
        # once within a particular group. 
        # If a user is already blocked in a group and you attempt to 
        # add another entry with the same user and group, it will 
        # raise an integrity error.

class Search(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    is_searching = models.BooleanField(default=False)




# Create your models here.
