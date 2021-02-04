from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager

from core.models import CoreModel


class Post(CoreModel):
    title = models.CharField(verbose_name="TITLE", max_length=50)
    content = models.TextField("CONTENT")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_prev(self):
        return self.get_previous_by_modified()

    def get_next(self):
        return self.get_next_by_modified()
