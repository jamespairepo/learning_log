from tkinter import CASCADE
from django.db import models


class Topic(models.Model):
    """a topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return str representation of model"""
        return self.text


class Entry(models.Model):
    """something specfic learning about a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """return a string representation of the model"""
        return f"{self.text[:50]}..."
