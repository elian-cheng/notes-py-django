from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)

    def __str__(self):
        return self.title
