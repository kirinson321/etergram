from django.db import models

# Create your models here.


class Tag(models.Model):
    """every available tag"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return string representation of the model"""
        return self.text


class Entry(models.Model):
    """entry containing a photo and a description"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a shortened string representation of the model"""
        return self.text[:50] + "..."
