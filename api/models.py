from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return self.title
    
    __str__ = __repr__
