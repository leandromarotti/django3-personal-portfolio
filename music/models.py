from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length = 50)
    album_name = models.CharField(max_length = 50)
    album_image = models.ImageField(upload_to = 'portfolio/images/')
    musicfile = models.FileField(upload_to = 'portfolio/music/')


    def __str__(self):
        return self.title
