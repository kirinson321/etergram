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
    photo = models.ImageField(upload_to='photos', default='/photos/default.jpg')
    date_added = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a shortened string representation of the model"""
        if(len(self.text) > 50):
            return self.text[:50] + "..."
        else:
            return self.text
