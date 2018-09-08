import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


User = get_user_model()

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True


class Invitation(TimeStampedModel):
    email_address = models.EmailField()
    name = models.CharField(max_length=250)
    token = models.CharField(max_length=64, unique=True)
    invited_by = models.ForeignKey(User, related_name='invitations', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.token = get_random_string(64)
        return super(Invitation, self).save(*args, **kwargs)

    def is_expired(self):
        expiry = self.created_at + datetime.timedelta(days=settings.INVITATION_EXPIRY)
        return self.created_at <= expiry
