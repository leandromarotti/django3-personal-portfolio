from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    article = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title
