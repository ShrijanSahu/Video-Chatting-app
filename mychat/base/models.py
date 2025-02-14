from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    uid = models.CharField(max_length=200, blank=False, null=False)
    room_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name