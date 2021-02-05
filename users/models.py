from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    profile_image = ProcessedImageField(
        upload_to="user/profile_image",
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )

    def __str__(self):
        return self.username
