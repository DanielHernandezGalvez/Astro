from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # create_at = models.DateTimeField(auto_created=True)
    create_at = models.DateTimeField(auto_now_add=True)