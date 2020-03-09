"""Research models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Research(models.Model):
    """Create the model for research."""

    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    scraped_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=250)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        """Rep title into a human readable form."""
        return "{} - {}".format(self.title, self.category)
