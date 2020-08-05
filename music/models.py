from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100)
    musicfile = models.FileField(upload_to = 'portfolio/music/')

    def __str__(self):
        return self.title
